import unittest
from fib import recursive_fib
from linked_list import LinkedList

class TestFib(unittest.TestCase):

    def test_invalid(self):
        with self.assertRaises(TypeError): # fails UNLESS exception is raised
             recursive_fib(-1)

        with self.assertRaises(TypeError): # fails UNLESS exception is raised
             recursive_fib(4.4)

        with self.assertRaises(TypeError): # fails UNLESS exception is raised
             recursive_fib(None)

    def test_base(self):
        # test our base case
        assert recursive_fib(0) == 0
        assert recursive_fib(1) == 1

    def test_large(self):
        assert recursive_fib(25) == 75025
        assert recursive_fib(13) == 233
        assert recursive_fib(6) == 8
        assert recursive_fib(19) == 4181

class TestLL:
    """ The main testing class that contains our unit tests. """

    def test_popValid(self):
        """ Test for valid bound complex numbers """

        ll = LinkedList(6)
        ll.push("hi")
        assert ll.pop() == "hi"
        ll.push("first in!")
        ll.push(8.8)
        ll.push(8.8)
        ll.push("last in!")
        assert ll.pop() == "last in!"
        ll2 = LinkedList(100)
        for i in range(1, 101):
            ll2.push(i)
        for i in range(1, 101):
            assert ll2.pop() == 101-i



if __name__ == '__main__':
    unittest.main()