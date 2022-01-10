def all_same(lst: list) -> bool:
    '''
    This will determine whether all the elements in the list are the same
    :param lst: the list that will be looked at
    :return: boolean of whether the every element is the same
    '''
    if lst is None:
        return True
    for i in lst:
        if lst[i] == lst[0]:
            continue
        else:
            return False
    return True


def dedup(lst: list) -> list:
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
    if lst is None:
        return 0
    max_run = 0
    curr = 0
    for i in lst:
        if i == lst[i-1:][0]:
            curr += 1
    if curr > max_run:
        max_run = curr
    return max_run


if __name__ == "__main__":
    a_list = [1, 4, 4, 4, -2, -2, -2, -2, 3, 1, 4]
    print(f"1. All same: {all_same(a_list)}")
    print(f"2. Dedup:    {dedup(a_list)}")
    print(f"3. Max run:  {max_run(a_list)}")