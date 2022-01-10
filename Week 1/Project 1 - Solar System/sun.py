

class Sun:
    def __init__(self, name: str, radius: float, mass: float, temperature: float):
        '''
        initializes the sun object
        :param name: name of the sun
        :param radius: radius of the given sun
        :param mass: mass of the sun object
        :param temperature: temperature of the sun object
        '''
        self.name = name
        self.radius = radius
        self.mass = mass
        self.temp = temperature

    def get_name(self):
        '''
        returns the name of the object
        :return: name of sun object
        '''
        return self.name

    def get_mass(self):
        '''
        returns the mass of the given sun object
        :return: mass of sun object
        '''
        return self.mass

    def get_radius(self):
        '''
        returns the radius of the given sun object
        :return: radius of the sun object
        '''
        return self.radius

    def get_temperature(self):
        '''
        returns temperature of given sun object
        :return: temperature of sun object
        '''
        return self.temp

    def __str__(self):
        '''
        magic operator that strings the name of the sun object
        :return: name of the object as a string
        '''
        return self.name


