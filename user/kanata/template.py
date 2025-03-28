pkgname = "kanata"
pkgver = "1.7.0"
pkgrel = 1
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Software keyboard remapper"
license = "LGPL-3.0-only"
url = "https://github.com/jtroo/kanata"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "eb7e11511f77558d72b5b3b0c9defb04b269637e5c8a4ad9b45d21382e9247d2"

if self.profile().wordsize == 32:
    broken = "needs atomic64"

if self.profile().arch in ["loongarch64"]:
    broken = "outdated nix crate, can't update"
