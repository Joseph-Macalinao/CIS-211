import unittest
import planet



class T0_TestPlanet(unittest.TestCase):
    def test_planet_build(self):
        p1 = planet.Planet('x25', 10.0, 100.0, 50.0)
        self.assertEqual(p1.name, 'x25')
        self.assertEqual(p1.radius, 10.0)
        self.assertEqual(p1.mass, 100.0)
        self.assertEqual(p1.distance, 50.0)



class T1_TestGetName(unittest.TestCase):
    def test_get_name(self):
        p1 = planet.Planet('x25', 10.0, 100.0, 50.0)
        self.assertEqual(p1.name, 'x25')

class T2_TestGetRadius(unittest.TestCase):
    def test_get_radius(self):
        p1 = planet.Planet('x25', 10.0, 100.0, 50.0)
        self.assertEqual(p1.radius, 10.0)

class T3_TestGetMass(unittest.TestCase):
    def test_get_mass(self):
        p1 = planet.Planet('x25', 10.0, 100.0, 50.0)
        self.assertEqual(p1.mass, 100.0)

class T4_TestGetDistance(unittest.TestCase):
    def test_get_distance(self):
        p1 = planet.Planet('x25', 10.0, 100.0, 50.0)
        self.assertEqual(p1.distance, 50.0)

class T5_TestGetVolume(unittest.TestCase):
    def test_get_volume(self):
        p1 = planet.Planet('x25', 10.0, 100.0, 50.0)
        self.assertEqual(p1.get_volume(), 4188.79)

class T6_TestGetSurfaceArea(unittest.TestCase):
    def test_get_surface_area(self):
        p1 = planet.Planet('x25', 10.0, 100.0, 50.0)
        self.assertEqual(p1.get_surface_area(), 1256.64)

class T7_TestGetDensity(unittest.TestCase):
    def test_get_density(self):
        p1 = planet.Planet('x25', 10.0, 100.0, 50.0)
        self.assertEqual(p1.get_density(), 0.02)

class T8_TestSetName(unittest.TestCase):
    def test_set_name(self):
        p1 = planet.Planet('x25', 10.0, 100.0, 50.0)
        p1.set_name('joe')
        self.assertEqual(p1.name, 'joe')

class T9_TestStringName(unittest.TestCase):
    def test_string_name(self):
        p1 = planet.Planet('x25', 10.0, 100.0, 50.0)
        self.assertEqual(p1.__str__(), 'x25')






if __name__ == "__main__":
    unittest.main(verbosity=2)


