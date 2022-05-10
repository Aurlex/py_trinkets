from py_trinkets import *

def clamp(val, max_val=None, min_val=None):
    if min_val != None and max_val != None:
        return max(min(val, max_val), min_val)
    elif min_val != None and max_val == None:
        return max(val, min_val)
    elif min_val == None and max_val != None:
        return min(val, max_val)


def move_toward(val, dest, step):
    if val < dest:
        val = clamp(val + step, dest)
    if val > dest:
        val = clamp(val - step, dest)
    return val
