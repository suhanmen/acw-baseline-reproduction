import sys
from typing import Union, Tuple

# Type alias for the input types
Number = Union[int, float]

def validate_inputs(a: Number, b: Number) -> Tuple[Number, Number]:
    """
    Validates that both inputs are numeric (int or float).
    Raises a TypeError if validation fails.

    Args:
        a: First number to compare.
        b: Second number to compare.

    Returns:
        A tuple containing the validated numbers.
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError(f"First argument must be a number, got {type(a).__name__}.")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError(f"Second argument must be a number, got {type(b).__name__}.")

    # Return the validated values explicitly
    return a, b

def minimum(a: Number, b: Number) -> Number:
    """
    Finds the minimum of two numbers using explicit comparison logic.

    This function does not rely on the built-in 'min' function to demonstrate
    explicit control flow and defensive programming practices as per the requirements.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The smaller of the two numbers.

    Raises:
        TypeError: If either argument is not a valid number (int or float)
                   or if either is a boolean (since bool is a subclass of int).
    """
    # Step 1: Validate inputs before performing any logic
    valid_a, valid_b = validate_inputs(a, b)

    # Step 2: Initialize the result variable with a default candidate
    # We start with the first number.
    result = valid_a

    # Step 3: Compare the second number to the current result
    # Using an explicit if-else statement for clarity and readability
    if valid_b < result:
        result = valid_b
    # If valid_b == result, we keep 'result' unchanged.
    # This handles the case where numbers are equal correctly.

    # Step 4: Return the determined minimum
    return result