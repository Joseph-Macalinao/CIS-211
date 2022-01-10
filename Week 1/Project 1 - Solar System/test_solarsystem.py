import unittest
import solarsystem


class T0_SolarSystemBuild(unittest.TestCase):
    def test_solar_build(self):
        ss = solarsystem.SolarSystem('Sun')
        self.assertEqual(ss.sun, 'Sun')
        self.assertEqual(ss.planets, [])

class T1_AddPlanets(unittest.TestCase):
    def test_add_planets(self):
        ss = solarsystem.SolarSystem('Sun')
        ss.add_planet('Saturn')
        self.assertEqual(ss.planets, ['Saturn'])

class T2_ShowPlanets(unittest.TestCase):
    def test_show_planets(self):
        ss = solarsystem.SolarSystem('Sun')
        ss.add_planet('Saturn')
        ss.add_planet('Uranus')