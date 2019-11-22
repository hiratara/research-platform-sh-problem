from publicsuffix2 import PublicSuffixList

psl = PublicSuffixList(psl_file="/tmp/public_suffix_list.dat")
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
    print(f"root: {psl.get_public_suffix(domain)}")
    print(f"public suffix: {psl.get_tld(domain)}")
    print()
