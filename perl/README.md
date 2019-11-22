```
$ carton install
$ carton exec -- perl ./psl.pl
[www.google.co.jp]
root: google.co.jp
public suffix: co.jp
tld: jp
error: (undef)

[foo.bar.yokohama.jp]
root: foo.bar.yokohama.jp
public suffix: bar.yokohama.jp
tld: jp
error: (undef)

[bar.yokohama.jp]
root: (undef)
public suffix: bar.yokohama.jp
tld: jp
error: Domain is already a suffix

[yokohama.jp]
root: (undef)
public suffix: yokohama.jp
tld: jp
error: Domain is already a suffix

[jp]
root: (undef)
public suffix: (undef)
tld: (undef)
error: Malformed domain

[foo.bar.platform.sh]
root: foo.bar.platform.sh
public suffix: bar.platform.sh
tld: sh
error: (undef)

[bar.platform.sh]
root: (undef)
public suffix: bar.platform.sh
tld: sh
error: Domain is already a suffix

[platform.sh]
root: (undef)
public suffix: platform.sh
tld: sh
error: Domain is already a suffix

[sh]
root: (undef)
public suffix: (undef)
tld: (undef)
error: Malformed domain

[foo.s3.amazonaws.com]
root: foo.s3.amazonaws.com
public suffix: s3.amazonaws.com
tld: com
error: (undef)

[s3.amazonaws.com]
root: (undef)
public suffix: s3.amazonaws.com
tld: com
error: Domain is already a suffix

[foo.s1.amazonaws.com]
root: s1.amazonaws.com
public suffix: amazonaws.com
tld: com
error: (undef)

[s1.amazonaws.com]
root: s1.amazonaws.com
public suffix: amazonaws.com
tld: com
error: (undef)
```
