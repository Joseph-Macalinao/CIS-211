import math
from sun import Sun
from solarsystem import SolarSystem


class Planet:
    def __init__(self, name: str, rad: float, mass: float, dist: float):
        self.__name = name
        self.__radius = rad
        self.__mass = mass
        self.__distance = dist

    def get_name(self):
        return self.__name

    def get_radius(self):
        return self.__radius

    def get_mass(self):
        return self.__mass

    def get_distance(self):
        return self.__distance

    def get_volume(self):
        volume = 4/3 * math.pi * self.__radius ** 3
        return volume

    def get_surface_area(self):
        sa = 4 * math.pi * self.__radius ** 2
        return sa

    def get_density(self):
        density = self.__mass / self.get_volume()
        return density

    def set_name(self, new_name):
        self.__name = new_name





