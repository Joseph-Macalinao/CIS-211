from planet import Planet
from solarsystem import SolarSystem

class Sun:
    def __init__(self, name: str, radius: float, mass: float, temp: float):
        self.__name = name
        self.__radius = radius
        self.__mass = mass
        self.__temp = temp

    def get_mass(self):
        return self.__mass

    def get_radius(self):
        return self.__radius

    def get_temp(self):
        return self.__temp

    def __str__(self):
        return self.__name


