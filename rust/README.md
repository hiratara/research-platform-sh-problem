```
$ cargo run

..snip..

[www.google.co.jp]
root: Some("google.co.jp")
public suffix: Some("co.jp")

[foo.bar.yokohama.jp]
root: Some("foo.bar.yokohama.jp")
public suffix: Some("bar.yokohama.jp")

[bar.yokohama.jp]
root: None
public suffix: Some("bar.yokohama.jp")

[yokohama.jp]
root: Some("yokohama.jp")
public suffix: Some("jp")

[jp]
root: None
public suffix: Some("jp")

[foo.bar.platform.sh]
root: Some("foo.bar.platform.sh")
public suffix: Some("bar.platform.sh")

[bar.platform.sh]
root: None
public suffix: Some("bar.platform.sh")

[platform.sh]
root: Some("platform.sh")
public suffix: Some("sh")

[sh]
root: None
public suffix: Some("sh")

[foo.s3.amazonaws.com]
root: Some("foo.s3.amazonaws.com")
public suffix: Some("s3.amazonaws.com")

[s3.amazonaws.com]
root: None
public suffix: Some("s3.amazonaws.com")

[foo.s1.amazonaws.com]
root: Some("amazonaws.com")
public suffix: Some("com")

[s1.amazonaws.com]
root: Some("amazonaws.com")
public suffix: Some("com")

[amazonaws.com]
root: Some("amazonaws.com")
public suffix: Some("com")
```
