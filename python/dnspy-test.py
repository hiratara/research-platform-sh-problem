from dnspy.dnspy import Dnspy

# XXX: The original Dnspy supports this keyword param, but not fork
# etld_url="file:///tmp/public_suffix_list.dat"
psl = Dnspy()

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
    subdoms = psl.subdoms(domain)
    print(f"root: {None if len(subdoms) < 2 else subdoms[1]}")
    print(f"public suffix: {psl.etld(domain)}")
    print()
