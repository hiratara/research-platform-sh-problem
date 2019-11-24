use publicsuffix::{errors, List};

fn main() -> errors::Result<()> {
    let psl = List::from_path("/tmp/public_suffix_list.dat")?;
    let domains = [
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
        "amazonaws.com",
    ];
    for domain in domains.iter() {
        let parsed = psl.parse_domain(domain)?;
        println!("[{}]", domain);
        println!("root: {:?}", parsed.root());
        println!("public suffix: {:?}", parsed.suffix());
        println!();
    }
    Ok(())
}
