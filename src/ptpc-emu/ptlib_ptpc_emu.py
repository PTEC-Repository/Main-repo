ver = '1.0-ALPHA'

import os

def getROM(path):
    with open(path, 'rb') as f:
        out = f.read()
    return out

def getMEM(path):
    with open(path, 'rb') as f:
        out = f.read()
    return out

def writeMEM(index, dec, path):
    MEM = getMEM(path)
    MEMobj = open(path, 'w+b')
    out = list()
    for i in MEM:
        out.append(i)
    MEMobj.write(bytearray(out))

def readMEM(index, path):
    out = getMEM(path)[index]
    return out
