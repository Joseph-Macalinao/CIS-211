"""
File: parser.py
A postfix expression parser.
"""
import expression


import logging
# To suppress DEBUG messages, level = logging.INFO
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('parser.py')


class Parser:
    """A small parser for reverse polish notation (RPN) calculator
    
    Examples:
        4 2 / is equivalent to (4 / 2)
        1 2 + 3 *  is equivalent to ((1 + 2) * 3)
        5 3 - 2 1 + *  is equivalent to ((5 - 3) * (2 + 1))
        5 3 - 2 1 + / 3 1 - * is equivalent to (((5 - 3) / (2 + 1)) * (3 - 1))
    """
    # Constant dictionary mapping operator symbols to expression classes in expression.py 
    OPS = {
        '+': expression.Add,
        '-': expression.Sub,
        '*': expression.Mul,
        '/': expression.Div
    }
    
    # A more specific error to use when raising parsing exceptions 
    # (also showing how we can defined classes inside other classes)
    class ParseError(Exception):
        def __init__(self, message: str):
            super().__init__(f"Calculator error: {message}")

    def __init__(self):
        """Initialize the parser"""
        self.parse_tree = None
                
    def parse(self, code: str) -> expression.Expression:
        """Parse the given postfix expression code string.
        
        Args: 
            code: a string containing an expression to be parsed
            
        Returns:
            An Expression object representing the root of the 
            parse tree of the expression.
        """
        # Add spaces around parentheses and operators, just in case
        for symbol in self.OPS:
            code = code.replace(symbol, ' ' + symbol + ' ')

        log.debug(f"Parsing: {code}")
        
        tokens = code.split()  # split the string into tokens
        log.debug(f"Tokens: {tokens}")

        # Using a stack to parse the postfix format
        stack = []
        index = 0
        while index < len(tokens):
            # TODO: complete the parsing loop, using the stack list:
            # The main steps:
            #   - Append (push) any int values to the stack. 
            #   - When the token is an operator, pop the left and right
            # operands from the stack. 
            #   - Then, create a new node with the operator and the two 
            # operands as children, and push (append) the new node to the stack.

            if tokens[index] in Parser.OPS.keys():
                if tokens[index] == '+':
                    log.debug(f"Adding Operator: {tokens[index]}")
                    right = stack.pop()
                    left = stack.pop()
                    expr = expression.Add(left, right)
                    stack.append(expr)
                elif tokens[index] == '-':
                    log.debug(f"Subtraction Operator: {tokens[index]}")
                    right = stack.pop()
                    left = stack.pop()
                    expr = expression.Sub(left, right)
                    stack.append(expr)
                elif tokens[index] == '*':
                    log.debug(f"Multiplication Operator: {tokens[index]}")
                    right = stack.pop()
                    left = stack.pop()
                    expr = expression.Mul(left, right)
                    stack.append(expr)
                elif tokens[index] == '/':
                    log.debug(f"Division Operator: {tokens[index]}")
                    right = stack.pop()
                    left = stack.pop()
                    expr = expression.Div(left, right)
                    stack.append(expr)
            elif type(tokens[index] == int):
                int_value = expression.IntValue(tokens[index])
                log.debug(f"Integer: {tokens[index]}")
                stack.append(int_value)

            index += 1

        # The tree root should be the only thing in the stack
        if len(stack) != 1:
            raise self.ParseError(f"Cannot process expression: {code}")

        log.debug("Parsed: " + str(stack[0]))
        self.parse_tree = stack[0]
        return stack[0]


if __name__ == '__main__':
    # Local tests
    parser = Parser()
    for exp in ('4 2 /', '5 3 - 2 1 + *', '5 3 - 2 1 + / 3 1 - *'):
        parse_tree = parser.parse(exp)
        log.info(f"{exp} = {parse_tree} = {parse_tree.evaluate()}")
