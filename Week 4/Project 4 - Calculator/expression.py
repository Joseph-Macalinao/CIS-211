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
        log.debug(f"{self.__class__.__name__} created")
        pass
    
    def __str__(self) -> str:
        raise NotImplementedError("__str__() is not implemented")
    
    def evaluate(self) -> int:
        raise NotImplementedError("evaluate() is not implemented")

# TODO: Implement the IntValue, BinOp, Add, Sub, Div and Mul classes following
# The inheritance structure described in Part 2

class BinOp(Expression):
    # TODO
    pass

class Add(BinOp):
    # TODO
    pass

class Sub(BinOp):
    # TODO
    pass

class Mul(BinOp):
    # TODO
    pass

class Div(BinOp):
    # TODO
    pass

