FitBlipper
==========

FitBlipper is a tool designed to help generate and check for the availability of bitflipped domain names and (g)TLDs.

(inspired by this (AWESOME) Defcon 21 presentation (https://www.youtube.com/watch?v=ZPbyDSvGasw || http://rot26.net/stucke.pdf || https://www.defcon.org/html/defcon-21/dc-21-speakers.html#Stucke)

**additional options**
```
$ ./fitblipper.py --help
usage: fitblipper.py [-h] [-s] [-a] [-f] -d DOMAIN

FitBlipper is a tool designed to help generate and check for the availability of bitflipped domain names.

optional arguments:
  -h, --help  show this help message and exit
  -s          list domains registered status
  -a          list only domains that are currently available for purchase
  -f          look for bitflipped (g)TLDs as well
  -d DOMAIN   the domain name to generate bitflip variants of
```

**tlds.txt**
This file contains the (g)TLDs that will also be tested for bit flipped variants.  It serves as a type of verification of valid (g)TLDs, if for example you do not wish to see `.bom` variants, you can remove `.bom` from the list.

**finding which domains to buy:**
```
$ ./fitblipper.py -fad microsoft.com
+====================+
| AVAILABLE DOMAINS: |
+====================+
+ testing 90 combinations... this may take a while...
microqoft.bom is available
microwoft.bom is available
eicrosoft.bom is available
microsgft.bom is available
micrnsoft.bom is available
micrgsoft.bom is available
microsodt.bom is available
miczosoft.bom is available
mkcrosoft.bom is available
mmcrosoft.bom is available
microsofv.bom is available
...
```

**finding all possible domains:**
```
$ ./fitblipper.py -fd microsoft.com
+=======================+
| ALL POSSIBLE DOMAINS: |
+=======================+
microsobt.com
micrmsoft.bom
macrosoft.com
micro3oft.bom
microcoft.com
mmcrosoft.bom
mibrosoft.bom
microqoft.bom
miarosoft.bom
micbosoft.bom
microroft.bom
migrosoft.com
microsofu.bom
microsofp.com
micvosoft.bom
microsnft.com
micrnsoft.com
miczosoft.com
licrosoft.bom
microsofd.bom
microsmft.bom
mkcrosoft.com
microqoft.com
micposoft.bom
micrgsoft.com
mikrosoft.bom
microskft.com
oicrosoft.com
eicrosoft.bom
microsont.com
eicrosoft.com
microsoft.com
microsogt.bom
microsodt.bom
microsofp.bom
microsofd.com
microsodt.com
mic2osoft.bom
microcoft.bom
microsovt.bom
iicrosoft.com
macrosoft.bom
microsgft.com
microwoft.com
microsmft.com
misrosoft.com
mibrosoft.com
microroft.com
micsosoft.com
miczosoft.bom
mhcrosoft.com
misrosoft.bom
microskft.bom
micrmsoft.com
microsnft.bom
microsgft.bom
micrgsoft.bom
oicrosoft.bom
micrksoft.bom
mycrosoft.bom
microwoft.bom
-icrosoft.com
mhcrosoft.bom
mmcrosoft.com
iicrosoft.bom
microsogt.com
microsoft.bom
-icrosoft.bom
micsosoft.bom
micposoft.com
microsobt.bom
migrosoft.bom
mycrosoft.com
microsofu.com
micbosoft.com
microsof4.com
miarosoft.com
microsofv.bom
microsovt.com
microsont.bom
micro3oft.com
micrnsoft.bom
micvosoft.com
microsof4.bom
microsofv.com
licrosoft.com
micrksoft.com
mikrosoft.com
mic2osoft.com
mkcrosoft.bom
```

