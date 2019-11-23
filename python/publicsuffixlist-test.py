from publicsuffixlist import PublicSuffixList

psl = None
with open("/tmp/public_suffix_list.dat", "rb") as f:
    psl = PublicSuffixList(f)

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
    print(f"root: {psl.privatesuffix(domain)}")
    print(f"public suffix: {psl.publicsuffix(domain)}")
    print()
