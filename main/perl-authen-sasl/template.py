pkgname = "perl-authen-sasl"
pkgver = "2.1700"
pkgrel = 1
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl", "perl-digest-hmac"]
depends = ["perl", "perl-digest-hmac"]
pkgdesc = "SASL authentication framework"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/release/Authen-SASL"
source = f"$(CPAN_SITE)/Authen/Authen-SASL-{pkgver}.tar.gz"
sha256 = "b86d5a576b8d387aee24f39f47a54afd14bb66b09003db5065001f1de03a8ece"
