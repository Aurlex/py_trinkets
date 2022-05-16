import keyboard, time, random

from py_trinkets.m import *
from py_trinkets.g import *
from py_trinkets.t import *


kinematic_bodies = []
hitboxes = []

grid = {}

file = StateDict("floor")
floor = file.unpack()
global_vars = StateDict("global_vars")
SIZE = global_vars.unpack()["SIZE"]


VIEWPORT_WIDTH = 20
VIEWPORT_HEIGHT = 20

PLAYER_MARKER = "@"
ENEMY_MARKER = "E"
HITBOX_MARKER = "x"

if not (SIZE, SIZE) in floor.keys():
    raise IndexError("Generated floor is smaller than terrain size")

for y in range(-SIZE, SIZE + 1):
    for x in range(-SIZE, SIZE + 1):
        grid[(x, y)] = [Vector2D(x, y), floor[(x, y)]]


class Hitbox(object):
    def __init__(
        self,
        position=Vector2D_ZERO(),
        left_bound=-1,
        right_bound=1,
        top_bound=-1,
        bottom_bound=1,
        name="A Hitbox",
    ):
        self.position = position

        self.left_bound = left_bound
        self.right_bound = right_bound
        self.top_bound = top_bound
        self.bottom_bound = bottom_bound
        self.name = name

        hitboxes.append(self)

    def is_colliding(self, other):
        # TODO: Create functionality for velocity input to create collision
        if (
            (other.right_bound - self.position.x)
            >= (self.left_bound - other.position.x)
            and (other.left_bound - self.position.x)
            <= (self.right_bound - other.position.x)
            and (other.bottom_bound - self.position.y)
            >= (self.top_bound - other.position.y)
            and (other.top_bound - self.position.y)
            <= (self.bottom_bound - other.position.y)
        ):
            return True


class KinematicBody(object):
    def __init__(self, hitbox_name, position):
        self.position = position
        self.velocity = Vector2D_ZERO()
        self.hitbox = Hitbox(
            position=position,
            left_bound=0,
            right_bound=0,
            top_bound=0,
            bottom_bound=0,
            name=hitbox_name,
        )
        kinematic_bodies.append(self)

    def collide(self, hitbox):
        if hitbox != self.hitbox:
            if hitbox.is_colliding(self.hitbox):
                return True

    def move(self):
        self.position += self.velocity
        self.position.x = clamp(self.position.x, SIZE - 1, -SIZE + 1)
        self.position.y = clamp(self.position.y, SIZE - 1, -SIZE + 1)
        self.hitbox.position = self.position


def update():
    global grid, hitboxes
    for y in range(-int(VIEWPORT_HEIGHT / 2), int(VIEWPORT_HEIGHT / 2) + 1):
        for x in range(-int(VIEWPORT_WIDTH / 2), int(VIEWPORT_WIDTH / 2) + 1):
            vx = x + Player.position.x
            vy = y + Player.position.y
            vector_val = Vector2D(vx, vy)
            if (vx, vy) in grid.keys():
                grid[(vx, vy)] = [vector_val, floor[(vx, vy)]]
            for hitbox in hitboxes:
                if (
                    (hitbox.right_bound - vx >= -hitbox.position.x)
                    and (hitbox.left_bound - vx <= -hitbox.position.x)
                    and (hitbox.bottom_bound - vy >= -hitbox.position.y)
                    and (hitbox.top_bound - vy <= -hitbox.position.y)
                ):
                    grid[(vx, vy)] = [vector_val, HITBOX_MARKER]

                if vector_val == hitbox.position:
                    if hitbox is Player.hitbox:
                        grid[(vx, vy)] = [vector_val, PLAYER_MARKER]
                    elif hitbox is Enemy.hitbox:
                        grid[(vx, vy)] = [vector_val, ENEMY_MARKER]
    draw()


def draw():
    global grid, SIZE
    clear()
    print(
        f"Player: {Player.position}, {Player.velocity}\nEnemy: {Enemy.position}, {Enemy.velocity}"
    )
    for y in range(-int(VIEWPORT_HEIGHT / 2), int(VIEWPORT_HEIGHT / 2) + 1):
        for x in range(-int(VIEWPORT_WIDTH / 2), int(VIEWPORT_WIDTH / 2) + 1):
            vx = x + Player.position.x
            vy = y + Player.position.y
            if (vx, vy) in grid.keys():
                if abs(vx) - abs(SIZE) == 0 or abs(vy) - abs(SIZE) == 0:
                    print("W", end=" ")
                else:
                    print(f"{grid[(vx, vy)][1]}", end=" ")
            else:
                print(" ", end=" ")
        print("\n", end="")


Wall = Hitbox(position=Vector2D(-2, -2), name="Wall")
Enemy = KinematicBody(position=Vector2D(20, -20), hitbox_name="Enemy")
Player = KinematicBody(position=Vector2D(0, 0), hitbox_name="Player")


update()
while True:

    if keyboard.is_pressed("w"):
        Player.velocity.y = -2
    elif keyboard.is_pressed("s"):
        Player.velocity.y = 2
    else:
        Player.velocity.y = 0

    if keyboard.is_pressed("a"):
        Player.velocity.x = -2
    elif keyboard.is_pressed("d"):
        Player.velocity.x = 2
    else:
        Player.velocity.x = 0

    Enemy.velocity = Vector2D(random.randint(-1, 1), random.randint(-1, 1))

    for body in kinematic_bodies:
        body.move()
        update()

    time.sleep(1 / 45)
