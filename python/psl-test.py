import psl

for domain in [
    "www.google.co.jp",
    "foo.bar.yokohama.jp",
    "bar.yokohama.jp",
    "yokohama.jp",
    "jp",
    "foo.bar.platform.sh",
    "bar.platform.sh",
    "platform.sh",
    "sh",
    "foo.s3.amazonaws.com",
    "s3.amazonaws.com",
    "foo.s1.amazonaws.com",
    "s1.amazonaws.com",
]:
    print(f"[{domain}]")
    s = psl.domain_suffixes(domain)
    print(f"root: {s.private}")
    print(f"public suffix: {s.public}")
    # print(f"can set cookie: {psl.domain_can_set_cookie(domain)}")
    print()
