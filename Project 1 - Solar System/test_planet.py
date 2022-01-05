import unittest
import planet



class T0_TestPlanet(unittest.TestCase):

    def test_planet_build(self):
        p1 = planet.Planet('x25', 10.0, 100.0, 50.0)
        self.assertEqual(p1.__name, 'x25')
        self.assertEqual(p1.__rad, 10.0)
        self.assertEqual(p1.__mass, 100.0)
        self.assertEqual(p1.__dist, 50.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)


