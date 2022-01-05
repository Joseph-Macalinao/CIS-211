


class SolarSystem:
    def __init__(self, sun):
        self.__sun = sun
        self.__planets = []

    def add_planets(self, planet):
        self.__planets.append(planet)

    def show_planets(self):
        for planet in self.__planets:
            print(planet)

