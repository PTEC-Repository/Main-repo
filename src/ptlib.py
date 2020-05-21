ver = 'DEVELOPMENT'

import time

def currTime():
    return time.strftime('%I:%M:%S%p')

def currDate():
    return time.strftime('%d/%m/%y')

def log(txt):
    print(time.strftime('%I:%M:%S%p(%d/%m/%y)=====================') + '\n' + txt + '\n')
    

