ver = '1.0'

import time
import os
import subprocess
import distutils.spawn

def currTime():
    return time.strftime('%I:%M:%S%p')

def currDate():
    return time.strftime('%d/%m/%y')

def log(txt):
    print(time.strftime('%I:%M:%S%p(%d/%m/%y)=====================') + '\n' + txt + '\n')
    
def shell(cmd):
    command = cmd.split(' ')
    proc = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    out = proc.communicate()[0]
    out = out.decode('ascii')
    return out

def command(cmd):
    os.system(cmd)

def catFile(fName):
    file = open(fName, 'r')
    return file.read()
    file.close()

def exists(path):
    return os.path.exists(path)

def isDir(path):
    if os.path.isdir(path):
        return True
    else:
        return False

def isFile(path):
    if os.path.isfile(path):
        return True
    else:
        return False

def echoToFile(path, txt):
    file = open(path, 'a+')
    file.write(txt)
    file.close()

def overwriteFile(path, txt):
    file = open(path, 'w')
    file.write(txt)
    file.close()

def checkBin(exe):
    if distutils.spawn.find_executable(exe):
        return True
    else:
        return False

def distro():
    dist = shell('lsb_release -a').splitlines()[1].split(' ')[1].split('\t')[1]
    return dist

def arch():
    return shell('uname -a').split(' ')[12]

def hostname():
    return shell('uname -a').split(' ')[1]

def distInstallPrompt(pkg):
    if distro() == 'Ubuntu':
        return 'sudo apt install ' + pkg
    elif distro() == 'Arch':
        return 'sudo pacman -S ' + pkg
    elif distro() == 'PTECOS':
        return 'ptpkg i ' + pkg + ' (or sudo pacman -S ' + pkg + ' failing that)'
     
def wget(URL, saveLocation):
    if checkBin('curl'):
        os.system('curl -s \'' + URL + '\' > ' + saveLocation)
    else:
        log('Curl Is Not Installed! It Needs To Be!\n' + distInstallPrompt('curl'))

def unZip(file, location):
    if isFile(file) and isDir(location):
        command('unzip \'' + file + '\' -d \'' + location + '\'')
    else:
        log('PTLIB: ERROR: unZip(): Input Not File Or Output Not Dir')












