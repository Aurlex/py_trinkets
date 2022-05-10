from py_trinkets import *
from dataclasses import dataclass
import math


class Vector2D:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return "({:g}, {:g})".format(self.x, self.y)

    def __repr__(self):
        return repr((self.x, self.y))

    def dot(self, other):

        if not isinstance(other, Vector2D):
            raise TypeError("Can only take dot product of two Vector2D objects")
        return self.x * other.x + self.y * other.y

    __matmul__ = dot

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):

        if isinstance(scalar, int) or isinstance(scalar, float):
            return Vector2D(self.x * scalar, self.y * scalar)
        raise NotImplementedError("Can only multiply Vector2D by a scalar")

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __truediv__(self, scalar):
        return Vector2D(self.x / scalar, self.y / scalar)

    def __mod__(self, scalar):
        return Vector2D(self.x % scalar, self.y % scalar)

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    def distance_to(self, other):
        return abs(self - other)

    def to_polar(self):
        return self.__abs__(), math.atan2(self.y, self.x)
