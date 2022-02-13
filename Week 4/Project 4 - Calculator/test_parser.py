# Run with python test_parser.py or Run->test_parser.py in CR
import unittest

# Import all classes from the parser.py module, you may also 
# wish to import things from expression.py
from parser import *

class Test_Parser(unittest.TestCase):
    # TODO: Create test methods __init__ and parse() methods
    # Make sure to have some with correct postfix expressions, and some without
    def test_init_parse(self):
        parse = Parser()
        self.assertEqual(parse.parse_tree, None)

    def test_parse(self):
        pars = Parser()
        self.assertEqual(str(pars.parse('4 2 /')), '(4 / 2)')

    def test_wrong_parse(self):
        pars = Parser()
        self.assertRaises(IndexError, pars.parse, '4 - 5')

    def test_empty(self):
        pars = Parser()
        self.assertRaises(pars.ParseError, pars.parse, '')


if __name__ == "__main__":
    unittest.main(verbosity=2)
