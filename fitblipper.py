#!/usr/bin/env python

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


import sys
import re
import os
import bitarray
import argparse

parser = argparse.ArgumentParser(description='FitBlipper is a tool designed to help generate and check for the availability of bitflipped domain names.')
parser.add_argument('-a', help='list only domains that are currently available for purchase', action="store_true")
parser.add_argument('-d', help='the domain name to generate bitflip variants of', dest="domain", required=True)
args = parser.parse_known_args()[0]

def domain_available(domain):
    ret = os.system("whois "+domain+" | grep -i 'no match' &>/dev/null")
    if ret == 0:
        return True
    else:
        return False

def main():
    if len(sys.argv) <= 1:
        parser.print_help()
    else:
        domain_in = args.domain
        tld = "com"
        if "." in domain_in :
            domain_in, tld = domain_in.split(".")
        results = {}
        bits = bitarray.bitarray()
        bits.fromstring(domain_in)
        bits_str = bits.to01()
        domain_valid = re.compile("^[a-z0-9\-]{1,}$")
        # chop into bytes
        for char in range(0,len(domain_in)):
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
        if args.a:
            sys.stderr.write("+====================+\n")
            sys.stderr.write("| AVAILABLE DOMAINS: |\n")
            sys.stderr.write("+====================+\n")
            for key, item in results.items():
                #Check if a whois record exists for this domain
                if domain_available(item+"."+tld):
                    print("%s.%s" % (item, tld))
                ##try: 
                ##    domain = whois.whois("%s.%s" % (item, tld))
                ##except:
                ##    print("%s.%s" % (item, tld))
        else:
            sys.stderr.write("+=======================+\n")
            sys.stderr.write("| ALL POSSIBLE DOMAINS: |\n")
            sys.stderr.write("+=======================+\n")
            for key, item in results.items():
                print("%s.%s" % (item, tld))

if __name__ == '__main__':
    main()
