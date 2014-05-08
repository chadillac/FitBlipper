FitBlipper
==========

A simple python script used to generate bit flipped versions of domain names.

(requires https://pypi.python.org/pypi/bitarray/)

(inspired by this (AWESOME) Defcon 21 presentation (https://www.youtube.com/watch?v=ZPbyDSvGasw || http://rot26.net/stucke.pdf || https://www.defcon.org/html/defcon-21/dc-21-speakers.html#Stucke)

**example usage:**
```
$ ./fitblipper.py microsoft
macrosoft.com
micposoft.com
mmcrosoft.com
microwoft.com
micrmsoft.com
micro3oft.com
micrgsoft.com
micrksoft.com
microcoft.com
microsont.com
micsosoft.com
micvosoft.com
mic2osoft.com
oicrosoft.com
microsof4.com
microsogt.com
micrnsoft.com
micbosoft.com
microsgft.com
microroft.com
misrosoft.com
iicrosoft.com
mikrosoft.com
miczosoft.com
miarosoft.com
microsmft.com
mibrosoft.com
eicrosoft.com
microqoft.com
microsovt.com
mkcrosoft.com
microsobt.com
microsofp.com
microsnft.com
microsofv.com
microsoft.com
microsofu.com
migrosoft.com
licrosoft.com
microsodt.com
microsofd.com
mhcrosoft.com
microskft.com
mycrosoft.com
```

**example usage for alternate TLDs:**
```
$ ./fitblipper.py microsoft.net
microsmft.net
misrosoft.net
micrmsoft.net
iicrosoft.net
mkcrosoft.net
mikrosoft.net
microsobt.net
micsosoft.net
mibrosoft.net
miczosoft.net
migrosoft.net
microsofd.net
microsont.net
micrnsoft.net
mic2osoft.net
microsofv.net
microsoft.net
microsofu.net
microsodt.net
microsofp.net
microsgft.net
micrksoft.net
mhcrosoft.net
mycrosoft.net
licrosoft.net
micbosoft.net
mmcrosoft.net
microwoft.net
microroft.net
macrosoft.net
eicrosoft.net
oicrosoft.net
microsovt.net
miarosoft.net
micrgsoft.net
microsnft.net
microsogt.net
micro3oft.net
micvosoft.net
microqoft.net
microsof4.net
micposoft.net
microcoft.net
microskft.net
```

**example usage for finding which domains to buy:**
```
$ ./fitblipper.py microsoft | xargs -n1 whois | grep -i 'no match' | grep -oEi "([A-Z0-9\-]){1,}.COM"
MIC2OSOFT.COM
OICROSOFT.COM
MICROSNFT.COM
MICROSONT.COM
MICROSOFV.COM
MICROSGFT.COM
MICRNSOFT.COM
MHCROSOFT.COM
MICROSOF4.COM
MICRO3OFT.COM
MICPOSOFT.COM
MICVOSOFT.COM
MICZOSOFT.COM
```
