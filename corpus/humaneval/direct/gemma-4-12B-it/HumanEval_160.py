def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """
    # To handle mathematical precedence correctly (e.g., multiplication before addition),
    # we construct the expression as a string and evaluate it.
    # We use 'eval' carefully here because the input format is specified as integers 
    # and specific operators.

    expression = str(operand[0])
    for i in range(len(operator)):
        op = operator[i]
        val = operand[i + 1]

        # Construct the string. We use // for floor division.
        expression += f" {op} {val}"

    # eval() respects standard PEMDAS rules.
    return eval(expression)