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
        self.name = name
        self.radius = rad
        self.mass = mass
        self.distance = dist

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
        sa = 4 * math.pi * self.radius ** 2
        return round(sa, 2)

    def get_density(self):
        density = self.mass / self.get_volume()
        return round(density, 2)

    def set_name(self, new_name):
        self.name = new_name




p1 = Planet('x25', 10.0, 100.0, 50.0)
print(p1.get_volume())
