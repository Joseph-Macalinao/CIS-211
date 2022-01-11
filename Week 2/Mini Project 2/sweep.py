def all_same(lst: list) -> bool:
    '''
    This will determine whether all the elements in the list are the same
    :param lst: the list that will be looked at
    :return: boolean of whether the every element is the same
    '''
    if lst is None:
        return True
    for i in lst:
        if i == lst[0]:
            continue
        else:
            return False
    return True


def dedup(lst: list) -> list:
    '''
    This function will return a list of which all immediately following duplicates will be removed
    :param lst: list being checked
    :return: list of removed duplicates
    '''
    if lst is None:
        return []
    ded = []
    for i in lst:
        if ded == []:
            ded.append(lst[0])
        elif i == ded[-1]:
            continue
        else:
            ded.append(i)
    return ded


def max_run(lst: list) -> int:
    '''
    This will find the "longest run" (repetition of same number in a row) in a list
    :param lst: list being looped through
    :return: Length of the longest list
    '''
    if lst is None:
        return 0
    max_run = 0
    curr = 1
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            curr += 1
        else:
            if curr > max_run:
                max_run = curr
            curr = 1
    return max_run


if __name__ == "__main__":
    a_list = [1, 4, 4, 4, -2, -2, -2, -2, 3, 1, 4]
    print(f"1. All same: {all_same(a_list)}")
    print(f"2. Dedup:    {dedup(a_list)}")
    print(f"3. Max run:  {max_run(a_list)}")