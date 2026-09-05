from typing import List, Union
from enum import Enum

class Token:
    def __init__(self, value: Union[int, str], is_operand: bool = True):
        self.value = value
        self.is_operand = is_operand

def validate_inputs(operator: List[str], operand: List[int]) -> None:
    """
    Validates the input lists for correctness according to the problem constraints.
    Raises ValueError if any validation check fails.
    """
    if operator is None:
        raise ValueError("Operator list cannot be None.")
    if operand is None:
        raise ValueError("Operand list cannot be None.")

    if len(operator) == 0:
        raise ValueError("Operator list must contain at least one operator.")
    if len(operand) == 0:
        raise ValueError("Operand list must contain at least one operand (constraint says >= 2, but >=1 is a minimal safety check).")

    # Constraint check: len(operator) == len(operand) - 1
    if len(operator) != len(operand) - 1:
        raise ValueError(f"Length mismatch: len(operator) must be exactly len(operand) - 1. "
                         f"Got len(operator)={len(operator)} and len(operand)={len(operand)}.")

    valid_operators = {'+', '-', '*', '//', '**'}
    for op in operator:
        if op not in valid_operators:
            raise ValueError(f"Invalid operator found: '{op}'. Valid operators are: +, -, *, //, **.")

    for op_val in operand:
        if not isinstance(op_val, int):
            raise ValueError(f"All operands must be integers. Found: {type(op_val)}")
        if op_val < 0:
            raise ValueError("All operands must be non-negative integers. Found negative value: " + str(op_val))

def parse_and_compute(operator: List[str], operand: List[int]) -> int:
    """
    Parses the operator and operand lists into a sequence of tokens and 
    computes the result using a stack-based approach respecting operator precedence.
    """
    # Step 1: Create a flat list of tokens [op1, val1, op2, val2, ...]
    # Format: Token(op), Token(val), Token(op), Token(val)...
    tokens: List[Token] = []

    for i, op_str in enumerate(operator):
        tokens.append(Token(op_str, is_operand=False))
        tokens.append(Token(operand[i], is_operand=True))

    # Append the last operand
    tokens.append(Token(operand[-1], is_operand=True))

    # Step 2: Define operator precedence levels
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '//': 2,
        '**': 3
    }

    # Step 3: Apply Shunting-yard algorithm or Two-Pass approach (Eval with precedence)
    # We will use a simplified Two-Pass approach (first pass for high precedence, second for low)
    # to keep it explicit and readable without external libraries.

    # Pass 1: Handle Exponentiation (**), Multiplication (*), Floor Division (//)
    # These bind tighter than + and -.
    # We will iterate and reduce these operations first.

    # Current state of the expression as a list of operands and high-precedence ops
    # Since the input is linear: val op1 val op2 val ...
    # We need to handle the structure carefully.

    # Let's convert the linear token list into a structure we can reduce.
    # Actually, a recursive descent or a stack-based evaluator is more robust.
    # Given the requirement for explicit steps, we will implement a simplified stack evaluator.

    values: List[int] = []
    ops: List[str] = []

    i = 0
    n_tokens = len(tokens)

    while i < n_tokens:
        token = tokens[i]

        if token.is_operand:
            values.append(token.value)
            i += 1
        else:
            op = token.value

            # Handle Operator Precedence
            # While there is an operator at the top of the ops stack and it has 
            # greater or equal precedence to the current operator, evaluate it.
            # Exception: Left-associativity means we process equal precedence immediately.

            while (len(ops) > 0):
                top_op = ops[-1]

                # Check precedence
                curr_prec = precedence.get(op, 0)
                top_prec = precedence.get(top_op, 0)

                # If top operator has higher or equal precedence, or if current is +/- and top is *//**
                # Note: For left-associative operators (+, -, *, //), if top_prec >= curr_prec, pop.
                # For right-associative (**), if top_prec > curr_prec, pop. If equal, keep (wait for next).
                # However, standard left-associative behavior for ** is often treated as right in math (2**3**2 = 2**(3**2)),
                # but in programming languages like Python, ** is right-associative.
                # Let's enforce Python's precedence rules:

                should_pop = False

                if top_prec > curr_prec:
                    should_pop = True
                elif top_prec == curr_prec:
                    if op in ('+', '-', '*', '//'):
                        should_pop = True # Left associative
                    else: # **
                        should_pop = False # Right associative

                if should_pop:
                    right_val = values.pop()
                    left_val = values.pop()
                    res = apply_operation(left_val, right_val, top_op)
                    values.append(res)
                    ops.pop()
                else:
                    break

            ops.append(op)
            i += 1

    # Pass 2: Process remaining operators (usually + and -)
    while len(ops) > 0:
        op = ops.pop()
        right_val = values.pop()
        left_val = values.pop()
        res = apply_operation(left_val, right_val, op)
        values.append(res)

    return values[0]

def apply_operation(left: int, right: int, op: str) -> int:
    """
    Executes a single arithmetic operation on two integer operands.
    Returns the result.
    """
    if op == '+':
        return left + right
    elif op == '-':
        return left - right
    elif op == '*':
        return left * right
    elif op == '//':
        # Python's // operator with negative numbers floors, but problem says non-negative inputs.
        # Even with non-negative, we use standard integer floor division.
        return left // right
    elif op == '**':
        return left ** right
    else:
        raise ValueError(f"Unknown operation encountered during execution: {op}")

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
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """
    # 1. Validation Phase
    validate_inputs(operator, operand)

    # 2. Parsing and Computation Phase
    result = parse_and_compute(operator, operand)

    return result