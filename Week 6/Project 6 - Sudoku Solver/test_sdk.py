"""Test cases for sdk.py"""

import unittest
from sdk_board import *
from sdk_config import *
import sdk_reader


class TestTileBasic(unittest.TestCase):
    def test_init_unknown(self):
        tile = Tile(3, 2, UNKNOWN)
        self.assertEqual(tile.row, 3)
        self.assertEqual(tile.col, 2)
        self.assertEqual(tile.value, '.')
        self.assertEqual(tile.candidates, set(CHOICES))
        self.assertEqual(repr(tile), "Tile(3, 2, '.')")
        self.assertEqual(str(tile), ".")

    def test_init_known(self):
        tile = Tile(5, 7, '9')
        self.assertEqual(tile.row, 5)
        self.assertEqual(tile.col, 7)
        self.assertEqual(tile.value, '9')
        self.assertEqual(tile.candidates, {'9'})
        self.assertEqual(repr(tile), "Tile(5, 7, '9')")
        self.assertEqual(str(tile), "9")


class TestBoardBuild(unittest.TestCase):

    def test_initial_board(self):
        board = Board()
        sample_tile = board.tiles[0][0]
        self.assertEqual(sample_tile.value, '.')
        sample_tile = board.tiles[3][3]
        self.assertEqual(sample_tile.value, '.')
        sample_tile = board.tiles[8][8]
        self.assertEqual(sample_tile.value, '.')

    def test_load_board(self):
        board = Board()
        board.set_tiles(["123456789", "2345678991", "345678912",
                         "456789123", "567891234", "678912345",
                         "789123456", "891234567", "912345678"])
        sample_tile = board.tiles[0][0]
        self.assertEqual(sample_tile.value, '1')
        sample_tile = board.tiles[3][5]
        self.assertEqual(sample_tile.value, '9')
        sample_tile = board.tiles[8][8]
        self.assertEqual(sample_tile.value, '8')


class TestBoardIO(unittest.TestCase):

    def test_read_new_board(self):
        board = sdk_reader.read(open("data/00-nakedsubset1.sdk"))
        as_printed = str(board)
        self.assertEqual(as_printed,
            "32...14..\n9..4.2..3\n..6.7...9\n8.1..5...\n...1.6...\n...7..1.8\n1...9.5..\n2..8.4..7\n..45...31")


class TestBoardGroups(unittest.TestCase):

    def test_count_tile_groups(self):
        """Every tile should appear in exactly three groups
        (regardless of board size).
        """
        board = Board()
        counts = { }
        for group in board.groups:
            for tile in group:
                if tile not in counts:
                    counts[tile] = 0
                counts[tile] += 1
        for tile in counts:
            self.assertEqual(counts[tile], 3)

    def test_groups_are_distinct(self):
        """Each group should contain a distinct set of tiles.
        (A frequent bug in Winter 2019 CIS 211.)
        """
        board = Board()
        groups_by_hash = { }
        for group in board.groups:
            hash_sum = 0
            for tile in group:
                hash_sum += hash(tile)
            self.assertNotIn(hash_sum, groups_by_hash,
                             msg=f"Oh no, group {group} is a duplicate!")
            groups_by_hash[hash_sum] = group


class TestConsistent(unittest.TestCase):
    """Tests of the 'is_consistent' method"""

    def test_good_complete_board(self):
        """This one is from Wikipedia"""
        board = Board()
        board.set_tiles(["534678912", "672195348", "198342567",
                        "859761423", "426853791", "713924856",
                         "961537284", "287419635", "345286179"])
        self.assertTrue(board.is_consistent())

    def test_good_incomplete(self):
        """From Sadman Sudoku"""
        board = Board()
        board.set_tiles(["...26.7.1", "68..7..9.", "19...45..",
                        "82.1...4.", "..46.29..", ".5...3.28",
                        "..93...74", ".4..5..36", "7.3.18..."])
        self.assertTrue(board.is_consistent())

    def test_bad_column(self):
        board = Board()
        board.set_tiles(["1........", ".........", ".........",
                         ".........", ".........", ".........",
                         "1........", ".........", "........."])
        self.assertFalse(board.is_consistent())

    def test_bad_row(self):
        board = Board()
        board.set_tiles([".........", ".........", ".........",
                         ".........", ".2.....2.", ".........",
                         ".........", ".........", "........."])
        self.assertFalse(board.is_consistent())

    def test_bad_block(self):
        board = Board()
        board.set_tiles([".........", "......1..", "........1",
                         ".........", ".........", ".........",
                         ".........", ".........", "........."])
        self.assertFalse(board.is_consistent())

class TestNakedSingle(unittest.TestCase):
    """Simple test of Naked Single using row, column, and block
    constraints.  From Sadman Sudoku,
    http://www.sadmansoftware.com/sudoku/nakedsingle.php
    """
    def test_sadman_example(self):
        board = Board()
        board.set_tiles([".........", "......1..", "......7..",
                         "......29.", "........4", ".83......",
                         "......5..", ".........", "........."])
        progress = board.naked_single()
        self.assertTrue(progress, "Should resolve one tile")
        progress = board.naked_single()
        self.assertTrue(progress, "A few candidates should be eliminated from other tiles")
        progress = board.naked_single()
        self.assertFalse(progress, "No more progress on this simple example")
        self.assertEqual(str(board),
            ".........\n......1..\n......7..\n......29.\n........4\n.83...6..\n......5..\n.........\n.........")

    def test_naked_single_one(self):
        """This puzzle can be solved with multiple rounds of naked single."""
        board = Board()
        board.set_tiles(["...26.7.1", "68..7..9.", "19...45..",
                         "82.1...4.", "..46.29..", ".5...3.28",
                         "..93...74", ".4..5..36", "7.3.18..."])
        board.solve()
        self.assertEqual(str(board),
                         "\n".join(["435269781", "682571493", "197834562",
                                    "826195347", "374682915", "951743628",
                                    "519326874", "248957136", "763418259"]))

if __name__ == "__main__":
    unittest.main()