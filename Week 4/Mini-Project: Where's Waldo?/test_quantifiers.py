"""Universal and existential quantifiers """

import unittest
from waldo import *


class TestAE(unittest.TestCase):
    """For all x, there exists y . P(y)"""

    # By row
    def test_exists_waldo_every_row(self):
        """For all rows in matrix, there exists a WALDO in the row"""
        self.assertTrue(all_row_exists_waldo([[OTHER, OTHER, WALDO, OTHER],
                                              [WALDO, OTHER, OTHER, OTHER],
                                              [WALDO, WALDO, WALDO, OTHER]]))
        self.assertFalse(all_row_exists_waldo([[OTHER, OTHER, WALDO],
                                               [OTHER, OTHER, OTHER],
                                               [WALDO, WALDO, WALDO]]))
        # Vacuous: No rows
        self.assertTrue(all_row_exists_waldo([]))
        # Vacuous: No columns
        self.assertFalse(all_row_exists_waldo([[],[]]))

    # By column
    def test_exists_waldo_every_col(self):
        """For all columns in the matrix, there exists a WALDO in the column"""
        self.assertTrue(all_col_exists_waldo([[OTHER, WALDO, OTHER],
                                              [WALDO, OTHER, OTHER],
                                              [OTHER, WALDO, WALDO]]))
        self.assertFalse(all_col_exists_waldo([[WALDO, OTHER, OTHER],
                                               [OTHER, WALDO, OTHER],
                                               [WALDO, OTHER, OTHER]]))

        # Vacuous: No rows
        self.assertTrue(all_col_exists_waldo([]))
        # Vacuous: No columns
        self.assertTrue(all_col_exists_waldo([[],[]]))

class TestAA(unittest.TestCase):
    """For all x, for all y . P(y)"""

    # By row
    def test_all_row_all_waldo(self):
        self.assertTrue(all_row_all_waldo([[WALDO, WALDO, WALDO],
                                           [WALDO, WALDO, WALDO],
                                           [WALDO, WALDO, WALDO]]))
        self.assertFalse(all_row_all_waldo([[WALDO, WALDO],
                                           [WALDO, OTHER],
                                           [WALDO, WALDO]]))
        # Vacuous: No rows
        self.assertTrue(all_row_all_waldo([]))
        # Vacuous: No columns
        self.assertTrue(all_row_all_waldo([[], [], []]))


    # By column
    def test_all_col_all_waldo(self):
        self.assertTrue(all_col_all_waldo([[WALDO, WALDO, WALDO],
                                           [WALDO, WALDO, WALDO],
                                           [WALDO, WALDO, WALDO]]))
        self.assertFalse(all_col_all_waldo([[WALDO, WALDO],
                                           [WALDO, OTHER],
                                           [WALDO, WALDO]]))
        # Vacuous: No rows
        self.assertTrue(all_row_all_waldo([]))
        # Vacuous: No columns
        self.assertTrue(all_row_all_waldo([[], [], []]))

class TestEE(unittest.TestCase):
    """There exists x such that there exists y . P(y)"""

    # By row
    def test_exists_row_exists_waldo(self):
        self.assertTrue(exists_row_exists_waldo([[OTHER, OTHER, OTHER],
                                                 [OTHER, OTHER, WALDO],
                                                 [OTHER, OTHER, OTHER]]))
        self.assertFalse(exists_row_exists_waldo([[OTHER, OTHER],
                                              [OTHER, OTHER]]))
        # Vacuous: No rows
        self.assertFalse(exists_row_exists_waldo([]))
        # Vacuous: No columns
        self.assertFalse(exists_row_exists_waldo([[], []]))

    # By column
    def test_exists_col_exists_waldo(self):
        self.assertTrue(exists_col_exists_waldo([[OTHER, OTHER, OTHER],
                                              [OTHER, OTHER, WALDO],
                                              [OTHER, OTHER, OTHER]]))
        self.assertFalse(exists_col_exists_waldo([[OTHER, OTHER],
                                          [OTHER, OTHER]]))

        # Vacuous: No rows
        self.assertFalse(exists_col_exists_waldo([]))
        # Vacuous: No columns
        self.assertFalse(exists_col_exists_waldo([[], []]))



class TestEA(unittest.TestCase):
    """There exists x such that all y . P(y)"""

    # By row
    def test_exists_row_all_waldo(self):

        self.assertTrue(exists_row_all_waldo([[OTHER, WALDO, OTHER],
                                              [WALDO, WALDO, WALDO],
                                              [OTHER, OTHER, OTHER]]))

        self.assertFalse(exists_row_all_waldo([[WALDO, OTHER, WALDO],
                                               [WALDO, OTHER, WALDO],
                                               [OTHER, WALDO, WALDO]]))

        #Vacuous: No rows
        self.assertFalse(exists_row_all_waldo([]))
        #Vacuous: No columns
        self.assertTrue(exists_row_all_waldo([[], []]))

    # By column
    def tests_exists_col_all_waldo(self):
        self.assertTrue(exists_col_all_waldo([[OTHER, WALDO, OTHER],
                                              [WALDO, WALDO, OTHER],
                                              [OTHER, WALDO, WALDO]]))

        self.assertFalse(exists_col_all_waldo([[WALDO, WALDO, WALDO],
                                               [WALDO, OTHER, WALDO],
                                               [OTHER, WALDO, OTHER]]))

        # Vacuous: No rows
        self.assertFalse(exists_col_all_waldo([]))
        # Vacuous: No columns
        self.assertFalse(exists_col_all_waldo([[], []]))


if __name__ == "__main__":
    unittest.main(verbosity=2)