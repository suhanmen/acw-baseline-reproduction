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
    import operator as op_module

    ops_map = {
        '+': op_module.add,
        '-': op_module.sub,
        '*': op_module.mul,
        '//': op_module.floordiv,
        '**': op_module.pow
    }

    # We need to respect operator precedence:
    # **, *, // have higher precedence than +, -
    # Among **, *, // they have same precedence, left-to-right
    # Among +, - they have same precedence, left-to-right

    # Step 1: Handle exponentiation first (highest precedence)
    # We will create a new list of operands and operators after collapsing exponentiations

    current_ops = list(operator)
    current_vals = list(operand)

    # Process exponentiations left-to-right
    i = 0
    while i < len(current_ops):
        if current_ops[i] == '**':
            # Pop current_vals[i+1], apply pow, push back result
            base = current_vals[i]
            exp = current_vals[i+1]
            result = base ** exp
            # Replace two operands and one operator with one result
            current_vals[i] = result
            # Remove next operand
            current_vals.pop(i+1)
            # Remove the ** operator
            current_ops.pop(i)
        else:
            i += 1

    # Step 2: Handle multiplication and floor division (same precedence, left-to-right)
    i = 0
    while i < len(current_ops):
        if current_ops[i] in ('*', '//'):
            left = current_vals[i]
            op_char = current_ops[i]
            right = current_vals[i+1]
            if op_char == '*':
                res = left * right
            else:
                res = left // right
            current_vals[i] = res
            current_vals.pop(i+1)
            current_ops.pop(i)
        else:
            i += 1

    # Step 3: Handle addition and subtraction (same precedence, left-to-right)
    i = 0
    while i < len(current_ops):
        left = current_vals[i]
        op_char = current_ops[i]
        right = current_vals[i+1]
        if op_char == '+':
            res = left + right
        else:  # '-'
            res = left - right
        current_vals[i] = res
        current_vals.pop(i+1)
        current_ops.pop(i)

    return current_vals[0]