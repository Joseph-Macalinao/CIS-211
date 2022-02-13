class Node:
    def __init__(self, NUMBER: int) -> None:
        self._data = NUMBER

    def sum_data(self) -> int:
        """sum the value"""
        raise NotImplementedError("Not implemented in the abstract Node class")
        
    def __str__(self) -> str:
        raise NotImplementedError("Not implemented in the abstract Node class")
    

class Leaf(Node):
    def __init__(self, data: int) -> None:
        super().__init__(data)

    def sum_data(self):
        return self._data

    def __str__(self) -> str:
        
        return f'{self._data}'


class Internal(Node):
    def __init__(self, data: int, left: Node, right: Node) -> None:
        super().__init__(data)
        self._left = left
        self._right = right


    def sum_data(self):
        '''numbers = []
        sum = 0

        numbers.append(self._data)
        numbers.append(self._left.sum_data())
        numbers.append(self._right.sum_data())
        for i in numbers:
            sum += i
        return sum'''
        return self._right.sum_data() + self._left.sum_data() + self._data

    def __str__(self) -> str:
        return f'<{self._data}, {self._left}, {self._right}>'
    

def main():
    l1 = Leaf(3)
    l2 = Leaf(6)
    l3 = Leaf(9)
    i = Internal(7, l2, l3)
    root = Internal(5, l1, i)
    print(root.sum_data())
    print(root)

if __name__ == '__main__':
    main()