import planet
import sun
import solarsystem


def main():
    '''
    Initializes whole program
    :return: none
    '''
    sun_1 = sun.Sun('Sun', 100, 1000000, 12345)
    earth = planet.Planet('Earth', 6465, 10000, 5678)
    solarsystem.SolarSystem(sun_1)


if __name__ == "__main__":
    main()

