# TODO: Follow the instructions in the HOWTO documents to implement this module.
# https://github.com/CIS-UO/Duck_Sudoku/blob/master/doc/HOWTO.md

# When done, this module will contain the following classes:
# Event, EventKind, Observer, TileEvent, TileObserver, Observable, Tile, Board

from typing import List, Sequence, Set

from sdk_config import CHOICES, UNKNOWN, ROOT
from sdk_config import NROWS, NCOLS

import enum

import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('board.py')


class Event(object):
    """
    Abstract base class of all events, both for MVC
    and for other purposes
    """
    pass


class EventKind(enum.Enum):
    TileChanged = 1
    TileGuessed = 2


class Observer(object):
    """
    Abstract base class for observers.
    Subclass this to make notification do something useful
    """
    def __init__(self):
        """
        Default constructor for simple observers w/out state
        """
        raise NotImplementedError("You have not implemented this function")

    def notify(self, event: Event):
        """
        Notify method of base class must be overridden in concrete classes
        :param event: event being sent
        :return:
        """
        raise NotImplementedError("You must override Observer.notify")


class TileEvent(Event):
    """
    Abstract base class for things that happen on tiles.
    We always indicate the tile. Concrete subclasses indicate nature
    of event
    """
    def __init__(self, tile: 'Tile', kind: 'EventKind'):
        self.tile = tile
        self.kind = kind
        # Note 'Tile" type is a forward reference;
        # Tile class is defined below

    def __str__(self):
        """Printed representation includes name of concrete subclass"""
        return f"{repr(self.tile)}"


class TileObserver(Observer):
    def notify(self, event: TileEvent):
        raise NotImplementedError("TileObserver subclass needs to override notify(TileEvent)")


class Observable:
    """Objects to which observers (like a view component) can be attached"""
    def __init__(self):
        self.observer = []

    def add_observer(self, observer: Observer):
        self.observer.append(observer)

    def notify_all(self, event: Event):
        for observer in self.observer:
            observer.notify(event)


class Tile(Observable):
    def __init__(self, row: int, col: int, value=UNKNOWN):
        super().__init__()
        assert value == UNKNOWN or value in CHOICES
        self.row = row
        self.col = col
        self.set_value(value)

    def set_value(self, value: str):
        '''
        setting tile value
        :param value: tile value
        :return:
        '''
        if value in CHOICES:
            self.value = value
            self.candidates = {value}
        else:
            self.value = UNKNOWN
            self.candidates = set(CHOICES)
        self.notify_all(TileEvent(self, EventKind.TileChanged))

    def __hash__(self) -> int:
        """Hash on position only (not value)"""
        return hash((self.row, self.col))

    def __str__(self):
        '''
        string magic method
        :return:
        '''
        return f"{self.value}"

    def __repr__(self):
        '''
        representations magic method
        :return:
        '''
        return f"Tile({self.row}, {self.col}, '{(self.value)}')"

    def could_be(self, value: str) -> bool:
        '''
        """Could be true iff value is a candidate value for this tile"""
        :param value: value of which the tile could be
        :return:
        '''
        return value in self.candidates

    def remove_candidates(self, used_values: Set[str]) -> bool:
        """The used values cannot be a value of this unknown tile.
        We remove those possibilities from the list of candidates.
        If there is exactly one candidate left, we set the
        value of the tile.

        Args:
            used_values:  set of values that cannot be candidates
        Returns:
            True means we eliminated at least one candidate,
            False means nothing changed (none of the 'used_values' was in our candidates set).
        """
        new_candidates = self.candidates.difference(used_values)
        if new_candidates == self.candidates:
            # Didn't remove any candidates
            return False
        self.candidates = new_candidates
        if len(self.candidates) == 1:
            self.set_value(new_candidates.pop())
        self.notify_all(TileEvent(self, EventKind.TileChanged))
        return True


class Board(object):
    """Board matrix of tiles"""
    def __init__(self):
        """Empty Board"""
        # Row/Column structure: Each row contains columns
        self.tiles: List[List[Tile]] = []
        for row in range(NROWS):
            cols = []
            for col in range(NCOLS):
                cols.append(Tile(row, col))
            self.tiles.append(cols)
        self.groups = []
        index = 0
        for row in self.tiles:
            self.groups.append(row)
        while index < len(self.tiles[0]):
            column = []
            for i in self.tiles:
                column.append(i[index])
            self.groups.append(column)
            index += 1
        for block_row in range(ROOT):
            for block_col in range(ROOT):
                group = []
                for row in range(ROOT):
                    for col in range(ROOT):
                        row_addr = (ROOT * block_row) + row
                        col_addr = (ROOT * block_col) + col
                        group.append(self.tiles[row_addr][col_addr])
                self.groups.append(group)

        log.debug(f"{self.groups}")

    def set_tiles(self, tile_values: Sequence[Sequence[str]]):
        '''
        """Set the tile values a list of lists or a list of strings"""
        :param tile_values: value of which the tile needs to be
        :return:
        '''
        for row_num in range(NROWS):
            for col_num in range(NCOLS):
                tile = self.tiles[row_num][col_num]
                tile.set_value(tile_values[row_num][col_num])

    def __str__(self) -> str:
        """In Sadman Sudoku format"""
        row_syms = []
        for row in self.tiles:
            values = [tile.value for tile in row]
            row_syms.append("".join(values))
        return "\n".join(row_syms)

    def is_consistent(self):
        '''
        checks to see if board works via being consistent
        :return:
        '''
        for group in self.groups:
            used_symbols = set()
            for tile in group:
                if tile.value in CHOICES:
                    if tile.value in used_symbols:
                        return False
                    else:
                        used_symbols.add(tile.value)
        return True

    def solve(self):
        '''
        """Solve the puzzle!"""
        :return: returns the puzzle solved (hopefully)
        '''
        progress = True
        while progress:
            progress = self.naked_single()
        return

    def naked_single(self) -> bool:
        """Eliminate candidates and check for sole remaining possibilities.

        Returns:
            True means we crossed off at least one candidate.
            False means we made no progress.
        """
        # tiles = set()
        # for i in self.tiles:
        #     for e in i:
        #         tiles[e] = []
        num_tile = 0
        for group in self.groups:
            used_symbols = set()
            for tile in group:
                if tile.value in CHOICES:
                    used_symbols.add(tile.value)
            for tile in group:
                if tile.value == UNKNOWN:
                    removed = tile.remove_candidates(used_symbols)
                    if removed:
                        num_tile += 1
        return num_tile > 0

    def hidden_single(self):
        '''
        attempts to solve certain parts of puzzle via "hidden single" method
        :return:
        '''
        results = False
        for group in self.groups:
            leftovers = set(CHOICES)
            for tile in group:
                if tile.value in CHOICES:
                    leftovers.discard(tile.value)
            for num in leftovers:
                num_counter = 0
                tiles_with_num = []
                for tile in group:
                    if num in tile.candidates:
                        num_counter += 1
                        tiles_with_num.append(tile)
                if num_counter == 1:
                    results = True
                    tiles_with_num[0].set_value(num)

        return results

    def is_complete(self):
        '''
        checks to see if board if complete
        :return:
        '''
        for row in self.tiles:
            for tile in row:
                if tile.value == UNKNOWN:
                    return False
        return True

    def min_choice_tile(self) -> Tile:
        """Returns a tile with value UNKNOWN and
        minimum number of candidates.
        Precondition: There is at least one tile
        with value UNKNOWN.
        """
        dictionary = {}
        num_candidates = set()

        for group in self.groups:
            for tile in group:
                if tile.value is UNKNOWN:
                    key_val = len(tile.candidates)
                    num_candidates.add(key_val)
                    dictionary.update({key_val: tile})
        min_value = min(num_candidates)
        first_empty = dictionary[min_value]
        return first_empty

    def propagate(self):
        '''
        """Repeat solution tactics until we
        don't make any progress, whether or not
        the board is solved.
        """
        :return: the board of a sudoku
        '''
        progress = True
        while progress:
            progress = self.naked_single()
            self.hidden_single()
        return








