import sun
import planet
from operator import attrgetter

class SolarSystem:
    def __init__(self, sun):
        '''
        Creates Solar System object
        :param sun: the sun used in the solar system
        '''
        self.sun = sun
        self.planets = []

    def add_planet(self, planet):
        '''
        how to add planets to given solar system object
        :param planet: planet being added
        :return: no return, changes solar system attribute
        '''
        self.planets.append(planet)

    def get_name(self):
        pass



    def show_planets(self, sortby='name'):
        '''
        shows the planets in a given solar system
        :return: no return
        '''
        if sortby == 'distance':
            for planet1 in sorted(self.planets, key=attrgetter("distance")):
                print(planet1)
        elif sortby == 'name':
            for planet1 in sorted(self.planets, key=attrgetter("name")):
                print(planet1)


