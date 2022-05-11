from py_trinkets import *


def clamp(val, max_val=None, min_val=None):
    """
    This function limits a value to a maximum and minimum

    `val`: Value to be clamped
    `max_val`: Maximum constraint
    `min_val`: Minimum constraint
    """
    if min_val != None and max_val != None:
        return max(min(val, max_val), min_val)
    elif min_val != None and max_val == None:
        return max(val, min_val)
    elif min_val == None and max_val != None:
        return min(val, max_val)


def move_toward(val, dest, step):
    """
    This function moves a value towards another value

    `val`: Value to move
    `dest`: Final value
    `step`: Step between values
    """
    if val < dest:
        val = clamp(val + abs(step), dest)
    if val > dest:
        val = clamp(val - abs(step), dest)
    return val
