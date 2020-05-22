ver = 'DEVELOPMENT'

import time
import os
import subprocess

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

def checkExists(path):
    return os.path.exists(path)

def echoToFile(path, txt):
    file = open(path, 'a+')
    file.write(txt)
    file.close()

def overwriteFile(path, txt):
    file = open(path, 'w')
    file.write(txt)
    file.close()
    
