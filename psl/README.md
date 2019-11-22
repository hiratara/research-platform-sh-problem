```
$ brew install libpsl
$ psl --load-psl-file /tmp/public_suffix_list.dat --print-unreg-domain www.google.co.jp foo.bar.yokohama.jp bar.yokohama.jp yokohama.jp jp foo.bar.platform.sh bar.platform.sh platform.sh sh foo.s3.amazonaws.com s3.amazonaws.com foo.s1.amazonaws.com s1.amazonaws.com
www.google.co.jp: co.jp
foo.bar.yokohama.jp: bar.yokohama.jp
bar.yokohama.jp: bar.yokohama.jp
yokohama.jp: yokohama.jp
jp: jp
foo.bar.platform.sh: bar.platform.sh
bar.platform.sh: bar.platform.sh
platform.sh: platform.sh
sh: sh
foo.s3.amazonaws.com: s3.amazonaws.com
s3.amazonaws.com: s3.amazonaws.com
foo.s1.amazonaws.com: com
s1.amazonaws.com: com
$ psl --load-psl-file /tmp/public_suffix_list.dat --print-reg-domain www.google.co.jp foo.bar.yokohama.jp bar.yokohama.jp yokohama.jp jp foo.bar.platform.sh bar.platform.sh platform.sh sh foo.s3.amazonaws.com s3.amazonaws.com foo.s1.amazonaws.com s1.amazonaws.com
www.google.co.jp: google.co.jp
foo.bar.yokohama.jp: foo.bar.yokohama.jp
bar.yokohama.jp: (null)
yokohama.jp: (null)
jp: (null)
foo.bar.platform.sh: foo.bar.platform.sh
bar.platform.sh: (null)
platform.sh: (null)
sh: (null)
foo.s3.amazonaws.com: foo.s3.amazonaws.com
s3.amazonaws.com: (null)
foo.s1.amazonaws.com: amazonaws.com
s1.amazonaws.com: amazonaws.com
```
