import random
from py_trinkets.t import StateDict


class bcolours:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    GREEN = "\033[32m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


SIZE = 20
TERRAIN = [
    ",",
    ".",
    "`",
    "'",
    ",",
    ".",
    "`",
    "'",
    ",",
    ".",
    "`",
    "'",
    "*",
]

file = StateDict("floor.test")
floor = {}

for y in range(-SIZE, SIZE + 1):
    for x in range(-SIZE, SIZE + 1):
        colour = bcolours.OKGREEN if random.randint(1, 2) == 2 else bcolours.GREEN
        floor[(x, y)] = (
            colour
            + TERRAIN[abs(random.randint(0, len(TERRAIN)) % len(TERRAIN))]
            + bcolours.ENDC
        )

file.append_dict(floor, overwrite=True)