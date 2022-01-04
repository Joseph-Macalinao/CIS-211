# Note about using Point as a type in type hints.
# Because Point is a user-defined class, it is not recognized
# as a type in type hints until we do the following:
from typing import TypeVar

Point = TypeVar("Point")

class Point:

    def __init__(self, x, y):
        """
        initializer of Point class
        :param x: int, what the x value of the point is
        :param y: int, what the y value of the point is
        return : object of Point class
        """
        self.x = x
        self.y = y

    def move(self, dx, dy):
        '''
        Moves the "point" object
        :param dx: how much the x value should change
        :param dy: how much the y value should change
        :return: NA
        '''
        self.x += dx
        self.y += dy

    def __eq__(self, points):
        '''
        Sees if a point is the same as another point object
        :param points: another point object to see if they are the same
        :return: boolean depending on if they are the same
        '''
        if self.x == points.x and self.y == points.y:
            return True
        else:
            return False

    def __str__(self):
        '''
        Returns the raw data of the Point coordinates
        :return: String value of the point coords
        '''
        return f'({self.x}, {self.y})'