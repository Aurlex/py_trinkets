from py_trinkets.g import *


def colour_interp(col1: list, col2: list, step: int) -> list:
    temp = col1
    step_val = 255 / step
    for x in range(step):
        temp = [
            move_toward(temp[0], col2[0], step_val),
            move_toward(temp[1], col2[1], step_val),
            move_toward(temp[2], col2[2], step_val),
        ]
        print(temp)


colour_interp([0, 0, 0], [255, 255, 255], 100)
