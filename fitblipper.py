#!/usr/bin/python

import sys
import re
import bitarray

def main():
    if len(sys.argv) <= 1:
        print('You need to give me a string... or run --help for info')
    elif sys.argv[1] == '--help':
        print("FitBlipper is a utility to flip single bits in domain a string to see what combinations are possible.\n")
        print("usage: fitblipper.py string_to_process")
    else:
        strang = sys.argv[1]
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
        for key, item in results.items():
            print(item+".com")

if __name__ == '__main__':
    main()
