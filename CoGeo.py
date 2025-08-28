import math

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Coordinate({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Coordinate):
            return Coordinate(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Coordinate):
            return Coordinate(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Coordinate(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)) and scalar != 0:
            return Coordinate(self.x / scalar, self.y / scalar)
        return NotImplemented

    def distance_to(self, other):
        if isinstance(other, Coordinate):
            return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        raise ValueError("Argument must be a Coordinate instance")

    def midpoint(self, other):
        if isinstance(other, Coordinate):
            return Coordinate((self.x + other.x) / 2, (self.y + other.y) / 2)
        raise ValueError("Argument must be a Coordinate instance")

    def slope(self, other):
        if isinstance(other, Coordinate):
            if self.x == other.x:
                raise ValueError("Slope is undefined for vertical line segments")
            return (other.y - self.y) / (other.x - self.x)
        raise ValueError("Argument must be a Coordinate instance")

    def __eq__(self, other):
        if isinstance(other, Coordinate):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)
