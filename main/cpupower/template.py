pkgname = "cpupower"
pkgver = "6.13.6"
pkgrel = 0
build_style = "makefile"
make_build_target = "cpupower"
make_build_args = [
    "-C",
    "tools",
    # FIXME: cpufreq-bench is completely broken with optimisations because of
    # int UB that gets optimised out and then breaks in div-by-zero
    "CPUFREQ_BENCH=0",
    "LLVM=1",
    "V=1",
    "NLS=false",
    "WERROR=0",
    "DEBUG=false",
    "STRIP=/bin/true",
    "libdir=/usr/lib",
    "mandir=/usr/share/man",
    "prefix=/usr",
    "sbindir=/usr/bin",
]
make_install_target = "cpupower_install"
make_install_args = [*make_build_args]
make_use_env = True
makedepends = [
    "libcap-devel",
    "libnl-devel",
    "linux-headers",
    "pciutils-devel",
]
pkgdesc = "Linux CPU power management tools"
license = "GPL-2.0-only"
url = "https://kernel.org"
source = f"https://cdn.kernel.org/pub/linux/kernel/v{pkgver[: pkgver.find('.')]}.x/linux-{pkgver}.tar.xz"
sha256 = "de0053cb413d408f20fd1d5788219951b8a4403e5dac1b1d9032090938acd199"
# nope
options = ["!check"]

if self.profile().arch == "x86_64":
    make_build_args += [
        "intel-speed-select",
        "turbostat",
        "x86_energy_perf_policy",
    ]
    make_install_args += [
        "intel-speed-select_install",
        "turbostat_install",
        "x86_energy_perf_policy_install",
    ]


@subpackage("cpupower-devel")
def _(self):
    return self.default_devel()
