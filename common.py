# -*- coding: utf-8 -*-

import sys
import imp

def errprint(fmt, args):
    sys.stderr.write(fmt % (args))

def make_hexver(major=2, minor=0, micro=0, release=0xF0):
    return (major<<24) + (minor<<16) + (micro<<8) + release

def make_strver(major=2, minor=0, micro=0, release=''):
    return format('%i.%i.%i%s' % (major, minor, micro, release))

def check_version(major, minor, micro):
    current_hexver = sys.hexversion
    current_strver = sys.version.split(' ')[0]
    require_hexver = make_hexver(major, minor, micro)
    require_strver = make_strver(major, minor, micro)
    if current_hexver < require_hexver:
        errprint('ERROR: %s requires python version %s or above.\n',
            (sys.argv[0], require_strver))
        errprint('       Current python version is %s\n', current_strver)
        sys.exit(1)

def check_module(modname):
    try:
        imp.find_module(modname)
    except ImportError:
        errprint('ERROR: %s requires %s module.\n', (sys.argv[0], modname))
        sys.exit(1)
