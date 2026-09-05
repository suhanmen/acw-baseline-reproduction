from typing import List, Any

def do_algebra(operator: List[str], operand: List[int]) -> int:
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
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.
    """

    # --- Input Validation ---
    if not isinstance(operator, list) or not isinstance(operand, list):
        raise TypeError("Both operator and operand must be lists.")

    if len(operand) < 2:
        raise ValueError("Operand list must contain at least two integers.")

    if len(operator) != len(operand) - 1:
        raise ValueError(
            f"Length mismatch: operator list size ({len(operator)}) "
            f"must be exactly one less than operand list size ({len(operand)})."
        )

    # Check if all operands are integers
    for i, val in enumerate(operand):
        if not isinstance(val, int):
            raise TypeError(f"Operand at index {i} is not an integer: {val}")
        if val < 0:
            raise ValueError(f"Operand at index {i} must be non-negative: {val}")

    # --- Expression Construction Logic ---
    # To correctly evaluate an algebraic expression, we must respect operator precedence:
    # 1. Exponentiation (**)
    # 2. Multiplication (*) and Floor Division (//)
    # 3. Addition (+) and Subtraction (-)

    # We represent the expression as a list of tuples: (value, operator, next_value)
    # However, to handle precedence without using `eval()` (which is unsafe), 
    # we can use a stack-based approach or a multi-pass approach.

    # Let's use a list of objects to represent terms: (value, operator_to_next)
    # Example: [2, '+', 3, '*', 4, '-', 5]
    # We will process this by identifying the precedence of each operator.

    def get_precedence(op: str) -> int:
        if op == '**':
            return 3
        if op in ('*', '//'):
            return 2
        if op in ('+', '-'):
            return 1
        return 0

    # Step 1: Handle Exponentiation (**) - Right-associative
    # Since we have to handle multiple operators, we'll process the list 
    # by looking for the highest precedence first.

    # Because the problem asks for the evaluation of "2 + 3 * 4 - 5",
    # and standard math rules apply, we should build the expression correctly.

    # A robust way to evaluate this without eval() is to treat it like a 
    # standard calculator expression parser.

    # Pass 1: Exponentiation (Right-to-Left)
    # Pass 2: Multiplication and Floor Division (Left-to-Right)
    # Pass 3: Addition and Subtraction (Left-to-Right)

    # Let's represent the state as a list of values and operators.
    # Initial state: [2, '+', 3, '*', 4, '-', 5]
    tokens = []
    for i in range(len(operand)):
        tokens.append(operand[i])
        if i < len(operator):
            tokens.append(operator[i])

    def evaluate_precedence(expression_tokens: List[Any], ops_to_handle: List[str], right_associative: bool) -> List[Any]:
        i = 0
        while i < len(expression_tokens):
            token = expression_tokens[i]
            if isinstance(token, str) and token in ops_to_handle:
                # Check if it's the highest precedence in the current scope
                # To simplify, we handle one precedence level at a time.
                # For right-associative (**), we need to find the rightmost occurrence.

                # This specific helper is used for standard left-associative logic.
                pass
            i += 1
        return expression_tokens

    # Refined logic: Process the list of tokens multiple times based on precedence.

    # 1. Exponentiation (**) - Right-to-Left
    # To handle right-to-left, we scan from right to left.
    idx = len(tokens) - 2
    while idx >= 0:
        op = tokens[idx]
        if op == '**':
            left_val = tokens[idx - 1]
            right_val = tokens[idx + 1]
            # Handle potential overflow or zero issues (though operands are non-negative)
            res = int(left_val ** right_val)
            # Replace the three tokens with the result
            tokens[idx - 1 : idx + 2] = [res]
            # After replacement, we need to check the new preceding operator
            # because we are moving backwards.
            idx -= 2 
        else:
            idx -= 1

    # 2. Multiplication (*) and Floor Division (//) - Left-to-Right
    i = 1
    while i < len(tokens):
        op = tokens[i]
        if op == '*' or op == '//':
            left_val = tokens[i - 1]
            right_val = tokens[i + 1]

            if op == '*':
                res = left_val * right_val
            else: # op == '//'
                if right_val == 0:
                    raise ZeroDivisionError("Floor division by zero is not allowed.")
                res = left_val // right_val

            tokens[i - 1 : i + 2] = [res]
            # After replacement, the next operator is now at the same index 'i'
            # because the list shrank. So we don't increment i.
        else:
            i += 1

    # 3. Addition (+) and Subtraction (-) - Left-to-Right
    i = 1
    while i < len(tokens):
        op = tokens[i]
        if op == '+' or op == '-':
            left_val = tokens[i - 1]
            right_val = tokens[i + 1]

            if op == '+':
                res = left_val + right_val
            else: # op == '-'
                res = left_val - right_val

            tokens[i - 1 : i + 2] = [res]
            # List shrank, stay at same index
        else:
            i += 1

    return int(tokens[0])