import ops
import iopc

pkg_path = ""
output_dir = ""
arch = ""
src_lib_dir = ""
dst_lib_dir = ""
pkg_tarball = "firmware.tar.xz"
pkg_sysroot_tarball = ""
pkg_tarball_dir = "firmware"
pkg_sysroot_tarball_dir = ""

def set_global(args):
    global pkg_path
    global output_dir
    global arch
    global src_lib_dir
    global dst_lib_dir
    global pkg_tarball
    global pkg_sysroot_tarball
    global pkg_tarball_dir
    global pkg_sysroot_tarball_dir

    pkg_path = args["pkg_path"]
    output_dir = args["output_path"]
    arch = ops.getEnv("ARCH_ALT")
    pkg_tarball = ops.path_join(pkg_path, pkg_tarball)
    pkg_tarball_dir = ops.path_join(output_dir, pkg_tarball_dir)

def MAIN_ENV(args):
    set_global(args)

    return False

def MAIN_EXTRACT(args):
    set_global(args)

    ops.unTarXz(pkg_tarball, output_dir)

    return True

def MAIN_PATCH(args, patch_group_name):
    set_global(args)
    for patch in iopc.get_patch_list(pkg_path, patch_group_name):
        if iopc.apply_patch(output_dir, patch):
            continue
        else:
            sys.exit(1)

    return True

def MAIN_CONFIGURE(args):
    set_global(args)
    return False

def MAIN_BUILD(args):
    set_global(args)

    return True

def MAIN_INSTALL(args):
    set_global(args)

    #iopc.installBin(args["pkg_name"], ops.path_join(dst_usr_lib_dir, "."), "usr/lib")

    return False

def MAIN_CLEAN_BUILD(args):
    set_global(args)
    return False

def MAIN(args):
    set_global(args)

