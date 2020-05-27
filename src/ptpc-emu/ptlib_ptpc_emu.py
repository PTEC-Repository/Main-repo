ver = '1.0-ALPHA'

import os

def getROM(path):
    with open(path, 'rb') as f:
        out = f.read()
    return out
