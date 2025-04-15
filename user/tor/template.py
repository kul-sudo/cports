pkgname = "tor"
pkgver = "0.4.8.16"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "pkgconf",
    "xz-devel",
    "asciidoc",
    "zstd-devel",
    "automake",
    "zlib-ng-compat-devel",
    "openssl3-devel",
    "libevent-devel",
]
pkgdesc = "Anonymizing overlay network"
license = "BSD-3-Clause"
url = "https://gitlab.com/torproject/tor"
source = f"{url}/-/archive/tor-{pkgver}/tor-tor-{pkgver}.tar.gz"
sha256 = "2964e2c3c7ebc9534595e59e29938e5446334510fdb912009cd877258898bfeb"
# requires shellcheck
options = ["!check"]


def post_install(self):
    self.install_file("src/config/torrc.sample.in", "etc/tor", name="torrc")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "tor")
    self.install_license("LICENSE")
