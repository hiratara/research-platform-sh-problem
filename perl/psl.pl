use strict;
use warnings;
use feature qw(say);
use Domain::PublicSuffix;

my $suffix = Domain::PublicSuffix->new({data_file => '/tmp/public_suffix_list.dat'});
for (qw(www.google.co.jp foo.bar.yokohama.jp bar.yokohama.jp yokohama.jp jp foo.bar.platform.sh bar.platform.sh platform.sh sh foo.s3.amazonaws.com s3.amazonaws.com foo.s1.amazonaws.com s1.amazonaws.com)) {
    my $root = $suffix->get_root_domain($_);
    say "[$_]";
    say "root: ", ($root // '(undef)');
    say "public suffix: ", ($suffix->suffix // '(undef)');
    say "tld: ", ($suffix->tld // '(undef)');
    say "error: ", ($suffix->error // '(undef)');
    say "";
}
