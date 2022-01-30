# TODO: Implement the 8 functions below, you can see examples in test_quantifiers.py


from provided import *     # some helper functions, feel free to use (or not)
from typing import List    # so we can specify list of list of string argument types

WALDO = 'W'
OTHER = '.'

# The matrix argument of all functions is a list of lists of strings

# for all, there exists


def all_row_exists_waldo(matrix: List[List[str]]) -> bool:
    """For all rows in the matrix, return True if WALDO is in some column"""
    for i in matrix:
        if WALDO not in i:
            return False
    return True


def all_col_exists_waldo(matrix: List[List[str]]) -> bool:
    """ For all columns in the matrix, return True if WALDO is in some row"""
    waldo = []
    if matrix == ([]):
        return True

    for i in matrix:
        index = 0
        for e in i:
            if e == WALDO:
                waldo.append(index)
            index += 1
    if sorted(set(waldo)) == [x for x in range(len(matrix[0]))]:
        return True
    return False


# for all, for all


def all_row_all_waldo(matrix: List[List[str]]) -> bool:
    """ For all rows in the matrix, return True if WALDO is in every column """
    for i in matrix:
        if OTHER in i:
            return False
    return True


def all_col_all_waldo(matrix: List[List[str]]) -> bool:
    """ For all the columns in the matrix, return True if WALDO is in every row """
    for i in matrix:
        if OTHER in i:
            return False
    return True

# there exists, for all


def exists_row_all_waldo(matrix: List[List[str]]) -> bool:
    """ Return True if here is some row in the matrix in which WALDO is in every column"""
    for i in matrix:
        if OTHER not in i:
            return True
    return False


def exists_col_all_waldo(matrix: List[List[str]]) -> bool:
    """ Return True if there is some column in the matrix in which WALDO is in every row"""
    index = 0
    lis = []
    if matrix == []:
        return False
    while index < len(matrix[0]):
        column = []
        for i in matrix:
            column.append(i[index])
        lis.append(column)
        index += 1
    for i in lis:
        if OTHER not in i:
            return True
    return False


# there exists, there exists


def exists_row_exists_waldo(matrix: List[List[str]]) -> bool:
    """ Return True if there is some row in the matrix in which WALDO is in some column"""
    for i in matrix:
        if WALDO in i:
            return True
        else:
            pass
    return False


def exists_col_exists_waldo(matrix: List[List[str]]) -> bool:
    """ Return True if there is some column in the matrix in which WALDO is in some row """
    for i in matrix:
        if WALDO in i:
            return True
        else:
            pass
    return False
