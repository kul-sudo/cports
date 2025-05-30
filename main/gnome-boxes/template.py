pkgname = "gnome-boxes"
pkgver = "48.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
]
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "gobject-introspection",
    "itstool",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "gtk+3-devel",
    "libarchive-devel",
    "libhandy-devel",
    "libosinfo-devel",
    "libportal-devel",
    "libsoup-devel",
    "libusb-devel",
    "libvirt-glib-devel",
    "libxml2-devel",
    "spice-gtk-devel",
    "webkitgtk-devel",
]
depends = [
    "libvirt",
    "qemu-img",
]
pkgdesc = "QEMU frontend for GNOME"
license = "GPL-2.0-only"
url = "https://apps.gnome.org/Boxes"
source = f"$(GNOME_SITE)/gnome-boxes/{'.'.join(pkgver.rsplit('.')[:-1])}/gnome-boxes-{pkgver}.tar.xz"
sha256 = "d05f5f42568fafbf6d88771161b06ed5f739d43121278d418cae95c56e513ead"
# gobject-introspection
# FIXME: lto makes the os-downloader crash (pick any os and it aborts instantly in os-downloader.vala)
options = ["!cross", "!lto"]

_arch = self.profile().arch
match _arch:
    case "x86_64" | "aarch64" | "loongarch64" | "riscv64":
        depends += [f"qemu-system-{_arch}"]
    case "ppc64le" | "ppc64":
        depends += ["qemu-system-ppc64"]


@subpackage("gnome-boxes-devel")
def _(self):
    return self.default_devel()
