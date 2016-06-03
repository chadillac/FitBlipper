FitBlipper
==========

A simple python script used to generate bit flipped versions of domain names.

(requires https://pypi.python.org/pypi/bitarray/)

(inspired by this (AWESOME) Defcon 21 presentation (https://www.youtube.com/watch?v=ZPbyDSvGasw || http://rot26.net/stucke.pdf || https://www.defcon.org/html/defcon-21/dc-21-speakers.html#Stucke)

**additional options**
```
usage: fitblipper.py [-h] [-a] -d DOMAIN

FitBlipper is a tool designed to help generate and check for the availability
of bitflipped domain names.

optional arguments:
  -h, --help  show this help message and exit
  -a          list only domains that are currently available for purchase
  -d DOMAIN   the domain name to generate bitflip variants of

```


**finding which domains to buy:**
```
$ ./fitblipper.py -ad microsoft.com 
+====================+
| AVAILABLE DOMAINS: |
+====================+
micrgsoft.com
microsmft.com
```

**finding all possible domains:**
```
$ ./fitblipper.py -d microsoft
+=======================+
| ALL POSSIBLE DOMAINS: |
+=======================+
micsosoft.com
micrgsoft.com
microsofd.com
microsofu.com
micrksoft.com
micvosoft.com
microcoft.com
microroft.com
mycrosoft.com
microsnft.com
miczosoft.com
mikrosoft.com
microsofv.com
micposoft.com
miarosoft.com
oicrosoft.com
microwoft.com
microsof4.com
microsogt.com
microsgft.com
microsodt.com
micrmsoft.com
mkcrosoft.com
microsoft.com
microsofp.com
macrosoft.com
microsont.com
microskft.com
eicrosoft.com
licrosoft.com
microsobt.com
mhcrosoft.com
micbosoft.com
misrosoft.com
migrosoft.com
microsovt.com
micrnsoft.com
mic2osoft.com
iicrosoft.com
micro3oft.com
microsmft.com
mmcrosoft.com
microqoft.com
mibrosoft.com
```

**using alternate TLDs:**
```
$ ./fitblipper.py -d microsoft.net
+=======================+
| ALL POSSIBLE DOMAINS: |
+=======================+
iicrosoft.net
microsmft.net
migrosoft.net
microqoft.net
microsof4.net
micro3oft.net
microroft.net
microsgft.net
macrosoft.net
microsofp.net
mikrosoft.net
mibrosoft.net
micrksoft.net
microsofd.net
micrnsoft.net
miczosoft.net
misrosoft.net
microsogt.net
microsobt.net
mhcrosoft.net
microcoft.net
eicrosoft.net
microsovt.net
micposoft.net
micrmsoft.net
microsofu.net
licrosoft.net
microsofv.net
miarosoft.net
microsoft.net
micbosoft.net
microwoft.net
mkcrosoft.net
micsosoft.net
microskft.net
microsnft.net
mic2osoft.net
mycrosoft.net
mmcrosoft.net
micvosoft.net
microsodt.net
micrgsoft.net
oicrosoft.net
microsont.net
```

