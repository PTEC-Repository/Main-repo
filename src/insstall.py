#!/usr/bin/env python3

ver = 'DEVELOPMENT'

import sys
import os

def installerUI():
    print('Installer UI Is Not Yet Implimented!, Exiting')
    exit()

try:
    home = os.environ['HOME']
    sys.path.append(home + '/PTEC/base/lib')
    import ptpkglib
except ModuleNotFoundError:
    ptlib.log('Error: Could Not Import ptpkglib, Exiting')
    exit()
try:
    home = os.environ['HOME']
    sys.path.append(home + '/PTEC/base/lib')
    import ptlib
except ModuleNotFoundError:
    ptlib.log('Error: Could Not Import ptlib, Exiting')
    exit()

ptlib.log('Modules ptlib and ptpkglib successfully loaded!')

if len(sys.argv) << 1:
    ptlib.log('No Commands Parsed! Starting UI!')
    installerUI()
else:
    options = sys.argv[1:]
