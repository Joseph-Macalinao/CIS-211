import unittest

# Import all classes from the expression.py module:
from expression import *

class Test_Expressions(unittest.TestCase):
    # TODO: Create test methods for the concrete classes:
    #       IntValue, Mul, Add, Sub, Div
    # You can test instantiation, __str__, and evaluate for each.
    # You can also write tests that ensure that you *cannot* instantiate
    # the abstract classes Expression and BinOp
    # Feel free to create separate Test_* classes if you prefer
    def test_int_init(self):
        inte = IntValue(5)
        self.assertEqual(inte._value, 5)

    def test_int_str(self):
        inte = IntValue(5)
        self.assertEqual(inte.__str__(), '5')

    def test_int_eval(self):
        inte = IntValue(5)
        self.assertEqual(inte.evaluate(), 5)

    def test_add_init(self):
        inte = Add(5, 6)
        self.assertEqual(inte.left, 6)
        self.assertEqual(inte.right, 5)

    def test_add_str(self):
        inte = Add(5, 6)
        self.assertEqual(inte.__str__(), '(5 + 6)')

    def test_add_eval(self):
        inte = Add(IntValue(5), IntValue(6))
        self.assertEqual(inte.evaluate(), 11)

    def test_sub_init(self):
        inte = Sub(5, 6)
        self.assertEqual(inte.left, 6)
        self.assertEqual(inte.right, 5)

    def test_sub_str(self):
        inte = Sub(5, 6)
        self.assertEqual(inte.__str__(), '(5 - 6)')

    def test_sub_eval(self):
        inte = Sub(IntValue(5), IntValue(6))
        self.assertEqual(inte.evaluate(), -1)

    def test_mul_init(self):
        inte = Mul(5, 6)
        self.assertEqual(inte.left, 6)
        self.assertEqual(inte.right, 5)

    def test_mul_str(self):
        inte = Mul(5, 6)
        self.assertEqual(inte.__str__(), '(5 * 6)')

    def test_mul_eval(self):
        inte = Mul(IntValue(5), IntValue(6))
        self.assertEqual(inte.evaluate(), 30)

    def test_div_init(self):
        inte = Div(14, 2)
        self.assertEqual(inte.left, 2)
        self.assertEqual(inte.right, 14)

    def test_div_str(self):
        inte = Div(14, 2)
        self.assertEqual(inte.__str__(), '(14 / 2)')

    def test_div_eval(self):
        inte = Div(IntValue(14), IntValue(2))
        self.assertEqual(inte.evaluate(), 7)



if __name__ == "__main__":
    unittest.main(verbosity=2)