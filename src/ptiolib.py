ver = '1.0'

import sys
import os

home = os.environ['HOME'] + '/'
sys.path.append(home + 'PTEC/base/lib/')

try:
    import ptlib
except ImportError:
    print('Cannot import PTEC ptlib')
    exit()

def hasBattery():
    if ptlib.exists('/sys/class/power_supply/BAT0') or ptlib.exists('/sys/class/power_supply/BAT1'):
        return True
    else:
        print('Bat Remove')
        return False

def batteryLocation():
    if hasBattery:
        if ptlib.exists('/sys/class/power_supply/BAT0/'):
            return '/sys/class/power_supply/BAT0'
        if ptlib.exists('/sys/class/power_supply/BAT1'):
            return '/sys/class/power_supply/BAT1/'

def battery():
    if hasBattery():
        out = ptlib.catFile(batteryLocation() + 'capacity').rstrip()
        return out
    else:
        return 'N/A'

def batteryStatus():
    if hasBattery():
        out = ptlib.catFile(batteryLocation() + 'status').rstrip()
        return out
    else:
        return 'N/A'

def thermalZones():
    out = ptlib.shell('ls /sys/class/thermal/').splitlines()
    outlst = list()
    thermalPath = '/sys/class/thermal/'
    for devName in out:
        if devName[0] == 't':
            outlst.append(thermalPath + devName)
    return outlst

def temp(zone):
    return ptlib.catFile(zone + '/temp').rstrip()


def hasBacklight():
    if len(ptlib.shell('ls /sys/class/backlight').splitlines()) > 0:
        return True
    else:
        return False

def backList():
    out = ptlib.shell('ls /sys/class/backlight').splitlines()
    return out

def getBrightness(backlight):
    out = ptlib.catFile('/sys/class/backlight/' + backlight + '/brightness')
    return out

def getMaxBrightness(backlight):
    out = ptlib.catFile('/sys/class/backlight/' + backlight + '/max_brightness')
    return out









