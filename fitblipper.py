## The MIT License (MIT)
## 
## Copyright (c) 2014 Chad Seaman
## 
## http://github.com/chadillac/FitBlipper
## 
## Permission is hereby granted, free of charge, to any person obtaining a copy
## of this software and associated documentation files (the "Software"), to deal
## in the Software without restriction, including without limitation the rights
## to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
## copies of the Software, and to permit persons to whom the Software is
## furnished to do so, subject to the following conditions:
## 
## The above copyright notice and this permission notice shall be included in all
## copies or substantial portions of the Software.
## 
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
## OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
## SOFTWARE.

#!/usr/bin/python

import sys
import re
import bitarray
import whois
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l', help='list of all the FitBlipper possible with the domain', action="store_true")
parser.add_argument('-a', help='list of all the available domains from the FitBlipper possibilities', action="store_true")
args, domain = parser.parse_known_args()

def main():
    if len(sys.argv) <= 1:
        print('You need to give me a string... or run --help for info')
    else:
        strang = sys.argv[1]
        tld = "com"
        if "." in sys.argv[1]:
            strang, tld = sys.argv[1].split(".")
        results = {}
        bits = bitarray.bitarray()
        bits.fromstring(strang)
        bits_str = bits.to01()
        domain_valid = re.compile("^[a-z0-9\-]{1,}$")
        # chop into bytes
        for char in range(0,strang.__len__()):
            start_off = char*8
            end_off = start_off+8
            char_bin = bits_str[start_off:end_off]
            char_ascii = bitarray.bitarray(char_bin)
            char_ascii = char_ascii.tostring()
            #print(char_bin, char_ascii)
            #flip single bits within the byte
            for bit_index in range(0,8):
                flipped_list = list(char_bin)
                flipped_list_orig = list(char_bin)
                bit = flipped_list[bit_index]
                if bit_index != 0:
                    flipped_list[bit_index] = str(1) if int(bit) == 0 else str(0)
                else:
                    continue
                flipped_list = ''.join(flipped_list)
                flipped_list_orig = ''.join(flipped_list_orig)
                flipped_ascii = bitarray.bitarray(flipped_list)
                flipped_ascii = flipped_ascii.tostring()
                #print (flipped_list_orig," => ",flipped_list," => ",flipped_ascii)
                flipped_result = ''.join([bits_str[:start_off], flipped_list, bits_str[end_off:]])
                flipped_result_ascii = bitarray.bitarray(flipped_result)
                flipped_result_ascii = flipped_result_ascii.tostring()
                flipped_result_ascii = flipped_result_ascii.lower()
                is_valid = domain_valid.findall(flipped_result_ascii)
                if len(is_valid) <= 0 or len(is_valid) > 1:
                    #print(flipped_result_ascii + " is invalid")
                    continue #invalid
                elif flipped_result_ascii[0] == "-" or flipped_result_ascii[-1] == "-":
                    #print(flipped_result_ascii + " is invalid")
                    continue #invalid
                else:
                    #print(flipped_result_ascii, is_valid)
                    #print (flipped_result, "=", flipped_result_ascii)
                    results[flipped_result_ascii] = flipped_result_ascii
        #print(bits.to01())
        #print(results.items())
        if args.l:
            for key, item in results.items():
                print("%s.%s"  % (item, tld))

        if args.a:
            for key, item in results.items():
                #Check if a whois record exists for this domain
                try: 
                    domain = whois.whois("%s.%s"  % (item, tld))
                except:
                    print("%s.%s"  % (item, tld))

        print("Following domain(s) are avaliable")
        for key, item in results.items():
            #Check if a whois record exists for this domain
            try: 
                domain = whois.whois("%s.%s"  % (item, tld))
            except:
                print("%s.%s"  % (item, tld))

if __name__ == '__main__':
    main()
