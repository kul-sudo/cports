pkgname = "vulkan-tools"
pkgver = "1.3.294"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DVULKAN_HEADERS_INSTALL_DIR=/usr",
    "-DBUILD_CUBE=ON",
]
hostmakedepends = [
    "cmake",
    "glslang-progs",
    "ninja",
    "pkgconf",
    "python",
]
makedepends = [
    "libxcb-devel",
    "libxkbcommon-devel",
    "libxrandr-devel",
    "linux-headers",
    "volk",
    "vulkan-headers",
    "vulkan-loader-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Official Vulkan tools and utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = (
    f"https://github.com/KhronosGroup/Vulkan-Tools/archive/v{pkgver}.tar.gz"
)
sha256 = "3eac1a3e4991b1c6ff92b29676f1291cf7fadd249cf6f142d5900af2e3179a51"
# CFI: vkcube etc fail
hardening = ["vis", "!cfi"]
# no test suite
options = ["!cross", "!check"]
