import math
import sun


class Planet:
    def __init__(self, name: str, radius: float, mass: float, distance: float):
        '''
        initializes a Planet object
        param name: name of the object
        param rad: radius of the object
        param mass: mass of the object
        param dist: distance of the object from the Sun
        '''
        self.name = name
        self.radius = radius
        self.mass = mass
        self.distance = distance

    def get_name(self):
        '''
        returns the name of given object
        return: name of object
        '''
        return self.name

    def get_radius(self):
        '''
        returns radius of given object
        return: radius of object
        '''
        return self.radius

    def get_mass(self):
        '''
        returns mass of given object
        return: mass of object
        '''
        return self.mass

    def get_distance(self):
        '''
        returns distance from sun of given object
        return: distance of given object
        '''
        return self.distance

    def get_volume(self):
        '''
        gives the volume of the given planet object
        return:
        '''
        volume = 4/3 * math.pi * self.radius ** 3
        return round(volume, 2)

    def get_surface_area(self):
        '''
        gives the surface area of the planet
        :return: sa of the planet
        '''
        sa = 4 * math.pi * self.radius ** 2
        return round(sa, 2)

    def get_density(self):
        '''
        gives the density of the given planet object
        :return: density of the planet
        '''
        density = self.mass / self.get_volume()
        return round(density, 2)

    def set_name(self, new_name):
        '''
        changes the name of a given planet object
        :param new_name: what the name will be changed to
        :return: new name of the object
        '''
        self.name = new_name

    def __str__(self):
        return self.name



