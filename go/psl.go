package main

import "fmt"
import "golang.org/x/net/publicsuffix"

func main() {
	domains := []string{
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
	};
	for _, domain := range domains {
		root, _ := publicsuffix.EffectiveTLDPlusOne(domain)
		publicSuffix, _ := publicsuffix.PublicSuffix(domain)
		fmt.Printf(
			"[%s]\nroot domain: %s\npublic suffix: %s\n\n",
			domain,
			root,
			publicSuffix,
		)
	}
}
