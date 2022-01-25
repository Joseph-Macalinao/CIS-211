def get_neighbors(list, coord: tuple, n_row, n_col, max_dist: int = 1): # -> List[tuple]:
    """Returns a list of neighboring individual closer than the max distance.

    Args:
        coord: The tuple of (row, col) coordinates of the individual.
        max_dist: The maximum distance of the neighbors to collect

    Returns:
        A list of coordinate tuples (row, col) of neighbors within
        within max_dist of the given coordinate.
    """
    # TODO: Implement for Part 1 with the default max_dist = 1, then extend for Part 2
    # to handle any distance within the grid. Do NOT return None values
    neighbors = []
    result = []
    if max_dist == 1:
        neighbors.extend([(coord[0] - 1, coord[1] - 1), (coord[0] - 1, coord[1]), (coord[0] - 1, coord[1] + 1),
                          (coord[0], coord[1] - 1), (coord[0], coord[1] + 1),
                          (coord[0] + 1, coord[1] - 1), (coord[0] + 1, coord[1]), (coord[0] + 1, coord[1] + 1)])

    elif max_dist == 2:
        neighbors.extend([(coord[0] - 2, coord[1] - 2), (coord[0] - 2, coord[1] - 1), (coord[0] - 2, coord[1] - 0),
                          (coord[0] - 2, coord[1] + 1), (coord[0] - 2, coord[1] + 2),
                          (coord[0] - 1, coord[1] - 2), (coord[0] - 1, coord[1] - 1), (coord[0] - 1, coord[1] - 0),
                          (coord[0] - 1, coord[1] + 1), (coord[0] - 2, coord[1] + 2),
                          (coord[0] - 0, coord[1] - 2), (coord[0] - 0, coord[1] - 1),
                          (coord[0] - 0, coord[1] + 1), (coord[0] - 2, coord[1] + 2),
                          (coord[0] + 1, coord[1] - 2), (coord[0] + 1, coord[1] - 1), (coord[0] + 1, coord[1] - 0),
                          (coord[0] + 1, coord[1] + 1), (coord[0] + 1, coord[1] + 2),
                          (coord[0] + 2, coord[1] - 2), (coord[0] + 2, coord[1] - 1), (coord[0] + 2, coord[1] - 0),
                          (coord[0] + 2, coord[1] + 2), (coord[0] + 2, coord[1] + 2)])
    for i in neighbors:
        if i[0] < 0 or i[0] > n_col - 1:
            pass
        elif i[1] < 0 or i[1] > n_row - 1:
            pass
        else:
            result.append(i)
    # for i in result:
    #     individual.append(Population.get_individual(self, i[1], i[0]))
    return result



list = [[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]]

print(get_neighbors(list, (4,4), 5, 5, max_dist=2))