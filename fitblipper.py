#!/usr/bin/env python3

## The MIT License (MIT)
## 
## Copyright (c) 2021 Chad Seaman
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
import argparse
import subprocess

parser = argparse.ArgumentParser(description='FitBlipper is a tool designed to help generate and check for the availability of bitflipped domain names.')
parser.add_argument('-s', help='list domains registered status', action="store_true")
parser.add_argument('-a', help='list only domains that are currently available for purchase', action="store_true")
parser.add_argument('-f', help='look for bitflipped (g)TLDs as well', action="store_true", dest="flip_it_all")
parser.add_argument('-d', help='the domain name to generate bitflip variants of', dest="domain", required=True)
args = parser.parse_known_args()[0]

def domain_available(domain):
    ret = os.system("whois '"+domain+"' | egrep -i '(no match|object does not)' &>/dev/null")
    if ret == 0:
        return True
    else:
        return False

def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

def frombits(bits):
    chars = []
    for b in range(int(len(bits) / 8)):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

def bitflip_it(dom_in, tld_in, flip_tld):
    # bitflipped variants cache
    bit_flipped = []

    # if we're doing TLD flipping as well, we'll
    # generate the TLD sublist first to ease building
    # of full domains next
    tld_list = [tld_in]
    if flip_tld:
        all_tlds = open('tlds.txt','r').read().split("\n")
        tld_bits = tobits(tld_in)
        for tld_off in range(len(tld_bits)):
            tld_tmp = tld_bits.copy()
            bit = tld_tmp[tld_off]
            if bit == 0:
                bit = 1
            else:
                bit = 0
            tld_tmp[tld_off] = bit
            tld_tmp = frombits(tld_tmp).lower()
            if is_valid(tld_tmp) and tld_tmp in all_tlds:
                if tld_tmp not in tld_list:
                    tld_list.append(tld_tmp)

    dom_bits = tobits(dom_in)
    for bit_off in range(len(dom_bits)):
        dom_tmp = dom_bits.copy()
        bit = dom_tmp[bit_off]
        if bit == 0:
            bit = 1
        else:
            bit = 0
        dom_tmp[bit_off] = bit
        dom_tmp = frombits(dom_tmp).lower()
        if is_valid(dom_tmp):
            for atld in tld_list:
                bit_flipped.append(dom_tmp+"."+atld)

    return bit_flipped

def is_valid(domain):
    valid_regex = re.compile("^[a-z0-9\-]{1,}$")
    valid_chars = valid_regex.findall(domain.lower())
    return (len(valid_chars) >= 1 and len(valid_chars[0]) == len(domain))

def main():
    if len(sys.argv) <= 1:
        parser.print_help()
    else:
        domain_in = args.domain
        tld = "com"
        if "." in domain_in :
            domain_in, tld = domain_in.split(".")
        results = {}

        domains = list(set(bitflip_it(domain_in, tld, args.flip_it_all)))

        if args.s or args.a:
            sys.stderr.write("+====================+\n")
            sys.stderr.write("| AVAILABLE DOMAINS: |\n")
            sys.stderr.write("+====================+\n")
            sys.stderr.write("+ testing "+str(len(domains))+" combinations... this may take a while...\n")
            for domain in domains:
                #Check if a whois record exists for this domain
                if domain_available(domain):
                    print("%s is available" % (domain))
                else: 
                    if args.s:
                        print("%s is registered" % (domain))
        else:
            sys.stderr.write("+=======================+\n")
            sys.stderr.write("| ALL POSSIBLE DOMAINS: |\n")
            sys.stderr.write("+=======================+\n")
            for domain in domains:
                print("%s" % (domain))

if __name__ == '__main__':
    main()
