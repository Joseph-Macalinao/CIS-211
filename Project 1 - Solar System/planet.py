import math



class Planet:
    def __init__(self, name: str, rad: float, mass: float, dist: float):
        '''
        initializes a Planet object
        param name: name of the object
        param rad: radius of the object
        param mass: mass of the object
        param dist: distance of the object from the Sun
        '''
        self.__name = name
        self.__radius = rad
        self.__mass = mass
        self.__distance = dist

    def get_name(self):
        '''
        returns the name of given object
        return: name of object
        '''
        return self.__name

    def get_radius(self):
        '''
        returns radius of given object
        return: radius of object
        '''
        return self.__radius

    def get_mass(self):
        '''
        returns mass of given object
        return: mass of object
        '''
        return self.__mass

    def get_distance(self):
        '''
        returns distance from sun of given object
        return: distance of given object
        '''
        return self.__distance

    def get_volume(self):
        '''
        gives the volume of the given planet object
        return:
        '''
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





