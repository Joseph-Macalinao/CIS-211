"""expression.py
Expression and BinOp abstract classes and their concrete subclasses for 
representing integer expressions containing +, -, *, /
"""

import logging
# To suppress DEBUG messages, level = logging.INFO
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('expression.py')


class Expression:
    """The abstract (base) class for all other expression node classes."""
    def __init__(self):
        '''
        initializes expression
        '''
        log.debug(f"{self.__class__.__name__} created")
        pass
    
    def __str__(self) -> str:
        '''
        abstract return nothing
        :return: None
        '''
        raise NotImplementedError("__str__() is not implemented")
    
    def evaluate(self) -> int:
        '''
        abstract return nothing
        :return: None
        '''
        raise NotImplementedError("evaluate() is not implemented")

# TODO: Implement the IntValue, BinOp, Add, Sub, Div and Mul classes following
# The inheritance structure described in Part 2


class BinOp(Expression):
    '''
    Abstract class to be used in the binary tree calculator
    '''
    def __init__(self, right, left):
        '''
        Initializes binop expression
        :param left: left node
        :param right: right node
        '''
        super(BinOp, self).__init__()
        self.left = left
        self.right = right

    def __str__(self):
        '''
        abstract return None
        :return: None
        '''
        raise NotImplementedError("__str__() is not implemented")

    def evaluate(self) -> int:
        '''
        abstract method return None
        :return: None
        '''
        raise NotImplementedError("evaluate() is not implemented")


class Add(BinOp):
    '''
    Adds two numbers together using the binary tree approach
    '''
    def __init__(self, right, left):
        '''
        Initializes add expression
        :param left: left node
        :param right: right node
        '''
        super(Add, self).__init__(right, left)

    def __str__(self):
        '''
        Gives the string of adding expressions
        :return: str
        '''
        return f'({self.right} + {self.left})'

    def evaluate(self) -> int:
        '''
        Evaluates the given expression of adding two expression/numbers
        :return: int
        '''
        return self.right.evaluate() + self.left.evaluate()


class Sub(BinOp):
    '''
    Subtracts two numbers together using the binary tree approach
    '''
    def __init__(self, right, left):
        '''
        Initializes subtract expression
        :param left: left node
        :param right: right node
        '''
        super(Sub, self).__init__(right, left)

    def __str__(self):
        '''
        Gives the string of subtracting expressions
        :return: str
        '''
        return f'({self.right} - {self.left})'

    def evaluate(self) -> int:
        '''
        Evaluates the given expression of subtracting two expression/numbers
        :return: int
        '''
        return self.right.evaluate() - self.left.evaluate()


class Mul(BinOp):
    '''
    Multiplies numbers together using a binary tree approach
    '''
    def __init__(self, right, left):
        '''
        Initializes multiply expression
        :param left: left node
        :param right: right node
        '''
        super(Mul, self).__init__(right, left)

    def __str__(self):
        '''
        Gives the string of multiplying expressions
        :return: str
        '''
        return f'({self.right} * {self.left})'

    def evaluate(self) -> int:
        '''
        Evaluates the given expression of multiplying two expression/numbers
        :return: int
        '''
        return self.right.evaluate() * self.left.evaluate()


class Div(BinOp):
    '''
    Divides two numbers using the binary tree approach
    '''
    def __init__(self, right, left):
        '''
        Initializes division expression
        :param left: left node
        :param right: right node
        '''
        super(Div, self).__init__(right, left)

    def __str__(self):
        '''
        Gives the string of dividing expressions
        :return: str
        '''
        return f'({self.right} / {self.left})'

    def evaluate(self) -> int:
        '''
        Evaluates the given expression of dividing two expression/numbers
        :return: int
        '''
        return int(self.right.evaluate() / self.left.evaluate())


class IntValue(Expression):
    '''
    Returns the value of a given node to be used by different operands in the binary tree
    '''
    def __init__(self, data):
        '''
        initializes intvalue node
        :param data: number for expression
        '''
        super().__init__()
        self._value = int(data)

    def __str__(self):
        '''
        Returns data of node as a string
        :return: str
        '''
        return f'{self._value}'

    def evaluate(self) -> int:
        '''
        Evaluates the node data by returning it
        :return: int
        '''
        return self._value

