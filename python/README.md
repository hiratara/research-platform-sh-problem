```
$ pipenv install --deploy
```

```
$ pipenv run -- python publicsuffix2-test.py
[www.google.co.jp]
root: google.co.jp
public suffix: co.jp

[foo.bar.yokohama.jp]
root: foo.bar.yokohama.jp
public suffix: bar.yokohama.jp

[bar.yokohama.jp]
root: bar.yokohama.jp
public suffix: yokohama.jp

[yokohama.jp]
root: yokohama.jp
public suffix: jp

[jp]
root: jp
public suffix: jp

[foo.bar.platform.sh]
root: foo.bar.platform.sh
public suffix: bar.platform.sh

[bar.platform.sh]
root: bar.platform.sh
public suffix: platform.sh

[platform.sh]
root: platform.sh
public suffix: sh

[sh]
root: sh
public suffix: sh

[foo.s3.amazonaws.com]
root: foo.s3.amazonaws.com
public suffix: s3.amazonaws.com

[s3.amazonaws.com]
root: s3.amazonaws.com
public suffix: amazonaws.com

[foo.s1.amazonaws.com]
root: s1.amazonaws.com
public suffix: amazonaws.com

[s1.amazonaws.com]
root: s1.amazonaws.com
public suffix: amazonaws.com
```

```
$ pipenv run -- python psl-test.py
[www.google.co.jp]
root: google.co.jp
public suffix: co.jp

[foo.bar.yokohama.jp]
root: foo.bar.yokohama.jp
public suffix: bar.yokohama.jp

[bar.yokohama.jp]
root: None
public suffix: bar.yokohama.jp

[yokohama.jp]
root: yokohama.jp
public suffix: jp

[jp]
root: None
public suffix: jp

[foo.bar.platform.sh]
root: foo.bar.platform.sh
public suffix: bar.platform.sh

[bar.platform.sh]
root: None
public suffix: bar.platform.sh

[platform.sh]
root: platform.sh
public suffix: sh

[sh]
root: None
public suffix: sh

[foo.s3.amazonaws.com]
root: foo.s3.amazonaws.com
public suffix: s3.amazonaws.com

[s3.amazonaws.com]
root: None
public suffix: s3.amazonaws.com

[foo.s1.amazonaws.com]
root: amazonaws.com
public suffix: com

[s1.amazonaws.com]
root: amazonaws.com
public suffix: com
```

```
$ pipenv run -- python publicsuffixlist-test.py
[www.google.co.jp]
root: google.co.jp
public suffix: co.jp

[foo.bar.yokohama.jp]
root: foo.bar.yokohama.jp
public suffix: bar.yokohama.jp

[bar.yokohama.jp]
root: None
public suffix: bar.yokohama.jp

[yokohama.jp]
root: yokohama.jp
public suffix: jp

[jp]
root: None
public suffix: jp

[foo.bar.platform.sh]
root: foo.bar.platform.sh
public suffix: bar.platform.sh

[bar.platform.sh]
root: None
public suffix: bar.platform.sh

[platform.sh]
root: platform.sh
public suffix: sh

[sh]
root: None
public suffix: sh

[foo.s3.amazonaws.com]
root: foo.s3.amazonaws.com
public suffix: s3.amazonaws.com

[s3.amazonaws.com]
root: None
public suffix: s3.amazonaws.com

[foo.s1.amazonaws.com]
root: amazonaws.com
public suffix: com

[s1.amazonaws.com]
root: amazonaws.com
public suffix: com
```
