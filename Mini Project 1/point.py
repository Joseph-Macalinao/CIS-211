# Note about using Point as a type in type hints.
# Because Point is a user-defined class, it is not recognized
# as a type in type hints until we do the following:
from typing import TypeVar

Point = TypeVar("Point")

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __eq__(self, points):
        if self.x == points.x and self.y == points.y:
            return True
        else:
            return False

    def __str__(self):
        return f'({self.x}, {self.y})'