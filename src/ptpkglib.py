ver = 'DEVELOPMENT'

import ptlib
import os
import sys

home = os.environ['HOME']
print('User home is: ' + home)

def checkInstall():
    if os.path.exists(home + '/PTEC/base/'):
        return True
    else:
        return False

def Install(pkg):

    sys.path.append(home + '/PTEC/base/lib')
    import ptlib
    import ptpkglib
    print('Imported PTEC Libries: ptlib')

    os.system('rm ~/PTEC/base/tmp/* -r')
    print('PTEC Tmp Directory Cleared')

def Remove(pkg):
    print('ptpkglib Remove Function Not Implimented')
