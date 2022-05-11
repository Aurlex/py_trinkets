from py_trinkets import *


class Vector2D(object):
    """
    Can be used to do complex spatial operations in 2D\n
    Data Type `Vector2D(x, y)`\n
        `x`: X component | `int, float`\n
        `y`: Y component | `int, float`
    
    See wiki for more details.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({:g}, {:g})".format(self.x, self.y)

    def __repr__(self):
        return repr((self.x, self.y))

    def __matmul__(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError("Can only take dot product of two Vector2D objects")
        return self.x * other.x + self.y * other.y

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector2D(self.x * other, self.y * other)
        if isinstance(other, Vector2D):
            return Vector2D(self.x * other.x, self.y * other.y)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector2D(self.x / other, self.y / other)
        if isinstance(other, Vector2D):
            return Vector2D(self.x / other.x, self.y / other.y)

    def __mod__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector2D(self.x % other, self.y % other)
        if isinstance(other, Vector2D):
            return Vector2D(self.x % other.x, self.y % other.y)

    def __abs__(self):
        return (self.x**2 + self.y**2) ** (1 / 2)

    def distance_to(self, other):
        """This function returns the distance to another `Vector2D`
        `other`: Other `Vector2D`
        """
        return abs(self - other)

    def normalise(self):
        """This function returns the normalised vector of a `Vector2D` 
        """
        if self.x != 0 or self.y != 0:
            magnitude = ((self.x**2) + (self.y**2)) ** (1 / 2)
            return Vector2D(self.x / magnitude, self.y / magnitude)
        else:
            return Vector2D(0, 0)


class Vector2D_ZERO(Vector2D):
    "Creates a `Vector2D` with a value of (0, 0)"
    def __init__(self):
        Vector2D.__init__(self, 0, 0)


class Vector2D_UP(Vector2D):
    "Creates a `Vector2D` with a value of (0, 0)"
    def __init__(self):
        Vector2D.__init__(self, 0, -1)


class Vector2D_DOWN(Vector2D):
    "Creates a `Vector2D` with a value of (0, 0)"
    def __init__(self):
        Vector2D.__init__(self, 0, 1)


class Vector2D_LEFT(Vector2D):
    "Creates a `Vector2D` with a value of (0, 0)"
    def __init__(self):
        Vector2D.__init__(self, -1, 0)


class Vector2D_RIGHT(Vector2D):
    "Creates a `Vector2D` with a value of (0, 0)"
    def __init__(self):
        Vector2D.__init__(self, 1, 0)
