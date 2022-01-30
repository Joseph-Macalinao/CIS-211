# Provided helper functions (you can use if you wish, but you don't have to)

from typing import List


def print_matrix(matrix: List[List[str]]):
    """Print a matrix row by row. """
    [print(''.join([v.center(3) for v in row])) for row in matrix]

def is_waldo_list(lst: List[str], waldo: str) -> bool:
    """Returns a list of values that are True if the corresponding 
    element in lst is WALDO, False otherwise.
    
    Args:
        lst: a list of strings
        waldo: a string to look for
    Returns:
        a list of booleans
        
    >>> is_waldo_list(['W', '.', 'W'], 'W')
    [True, False, True]
    
    >>> is_waldo_list([], 'W')
    []
    """
    return [element == waldo for element in lst]

def nrows(matrix: List[List[str]]) -> int:
    """Returns the number of rows in the matrix."""
    try:
        return len(matrix)
    except:
        return 0

def ncols(matrix: List[List[str]]) -> int:
    """Returns the number of columns in the matrix."""
    try:
        return len(matrix[0])
    except: 
        return 0