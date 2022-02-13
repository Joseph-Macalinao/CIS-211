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
        return f"{self.value}"

    def __repr__(self):
        return f"Tile({self.row}, {self.col}, '{(self.value)}')"

    def could_be(self, value: str) -> bool:
        """Could be true iff value is a candidate value for this tile"""
        return value in self.candidates


class Board(object):
    """Board matrix of tiles"""
    def __init__(self):
        """Empty Board"""
        # Row/Column structure: Each row contains columns
        self.tiles: List[List[Tile]] = []
        for row in range(NROWS):
            cols =[]
            for col in range(NCOLS):
                cols.append(Tile(row, col))
            self.tiles.append(cols)
        self.groups = []
        for row in self.tiles:
            self.groups.append(row)
        for i in range(NCOLS):
            cols = []
            for e in range(i):
                if e.__index__() == i:
                    cols.append(Tile(i,e))
                self.groups.append(cols)

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
        """Set the tile values a list of lists or a list of strings"""
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
        """
        for each group (row, column, or block):
            used symbols = { }
            for each tile in the group:
                if the tile is one of CHOICES (anything but UNKNOWN):
                    if the tile's symbol is already in used symbols:
                        return False (board is not consistent)
                    else:
                        add the tile's symbol to the used symbols
        return True  (the solved part of the board is ok so far)
        :return:
        """


    def solve(self):
        """Solve the puzzle!"""
        #FIXME: This will be added in the next step
        return







