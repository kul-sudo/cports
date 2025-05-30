pkgname = "jansson"
pkgver = "2.14"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "slibtool"]
pkgdesc = "Library for encoding, decoding and manipulating JSON data"
license = "MIT"
url = "https://www.digip.org/jansson"
source = f"https://github.com/akheron/jansson/releases/download/v{pkgver}/jansson-{pkgver}.tar.gz"
sha256 = "5798d010e41cf8d76b66236cfb2f2543c8d082181d16bc3085ab49538d4b9929"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("jansson-devel")
def _(self):
    return self.default_devel()
