import platform
from os.path import dirname, abspath


def getcwebp():
    if platform.system() == 'Linux':
        return dirname(dirname(abspath(__file__))) + '/lib/libwebp_linux/bin/cwebp'
    elif platform.system() == 'Windows':
        arch = platform.architecture()
        if arch[0] == '64bit':
            return dirname(dirname(abspath(__file__))) + '/lib/libwebp_win64/bin/cwebp.exe'
        elif arch[0] == '32bit' and arch[0] == '86bit':
            return dirname(dirname(abspath(__file__))) + '/lib/libwebp_win32/bin/cwebp.exe'
    elif platform.system() == 'Darwin':
        return dirname(dirname(abspath(__file__))) + '/lib/libwebp_osx/bin/cwebp'
    else:
        print('Unsupported platform:', platform.system(), platform.architecture())


def getdwebp():
    if platform.system() == 'Linux':
        return dirname(dirname(abspath(__file__))) + '/lib/libwebp_linux/bin/dwebp'
    elif platform.system() == 'Windows':
        arch = platform.architecture()
        if arch[0] == '64bit':
            return dirname(dirname(abspath(__file__))) + '/lib/libwebp_win64/bin/dwebp.exe'
        elif arch[0] == '32bit' and arch[0] == '86bit':
            return dirname(dirname(abspath(__file__))) + '/lib/libwebp_win32/bin/dwebp.exe'
    elif platform.system() == 'Darwin':
        return dirname(dirname(abspath(__file__))) + '/lib/libwebp_osx/bin/dwebp'
    else:
        print('Unsupported platform:', platform.system(), platform.architecture())


def getgifwebp():
    if platform.system() == 'Linux':
        return dirname(dirname(abspath(__file__))) + '/lib/libwebp_linux/bin/gif2webp'
    elif platform.system() == 'Windows':
        arch = platform.architecture()
        if arch[0] == '64bit':
            return dirname(dirname(abspath(__file__))) + '/lib/libwebp_win64/bin/gif2webp.exe'
        elif arch[0] == '32bit' and arch[0] == '86bit':
            return dirname(dirname(abspath(__file__))) + '/lib/libwebp_win32/bin/gif2webp.exe'
    elif platform.system() == 'Darwin':
        return dirname(dirname(abspath(__file__))) + '/lib/libwebp_osx/bin/gif2webp'
    else:
        print('Unsupported platform:', platform.system(), platform.architecture())


def getwebpmux():
    if platform.system() == 'Linux':
        return dirname(dirname(abspath(__file__))) + '/lib/libwebp_linux/bin/webpmux'
    elif platform.system() == 'Windows':
        arch = platform.architecture()
        if arch[0] == '64bit':
            return dirname(dirname(abspath(__file__))) + '/lib/libwebp_win64/bin/webpmux.exe'
        elif arch[0] == '32bit' and arch[0] == '86bit':
            return dirname(dirname(abspath(__file__))) + '/lib/libwebp_win32/bin/webpmux.exe'
    elif platform.system() == 'Darwin':
        return dirname(dirname(abspath(__file__))) + '/lib/libwebp_osx/bin/webpmux'
    else:
        print('Unsupported platform:', platform.system(), platform.architecture())
