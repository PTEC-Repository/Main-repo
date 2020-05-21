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

def Install():

    sys.path.append(home + '/PTEC/base/lib')
    import ptlib
    import ptpkglib
    print('Imported PTEC Libries: ptlib')

    os.system('rm ~/PTEC/base/tmp/* -r')
    print('PTEC Tmp Directory Cleared')

    Path = input('Path Of PTPKG File:')

    if os.path.isfile(Path):
        print('Installing: ' + Path)
    elif os.path.isdir(Path):
        print('Path \'' + Path + '\' Is a Directory. Exiting')
        exit()
    else:
        print('\'' + Path + '\' Is Not Existent, Not a File or Not Valid. Exiting')
        exit()

