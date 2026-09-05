from typing import Tuple, Optional, Union

Number = Union[int, float]

def is_valid_positive_integer(value: Number) -> bool:
    """
    Check if the given value is a positive integer.

    Args:
        value: The value to check

    Returns:
        True if value is a positive integer, False otherwise
    """
    if not isinstance(value, int):
        return False

    # Must be strictly positive (greater than 0)
    if value <= 0:
        return False

    return True

def validate_inputs(a: Number, b: Number) -> Tuple[Optional[int], Optional[int]]:
    """
    Validate that both inputs are positive integers.

    Returns:
        A tuple of (a, b) if both are valid positive integers,
        (None, None) otherwise.
    """
    if not is_valid_positive_integer(a):
        return None, None

    if not is_valid_positive_integer(b):
        return None, None

    return a, b

def gcd_helper(m: int, n: int) -> int:
    """
    Helper function to compute GCD using the Euclidean algorithm.

    This function assumes both m and n are already validated as positive integers.
    It uses a while loop for explicit control flow.

    Args:
        m: First positive integer
        n: Second positive integer

    Returns:
        The greatest common divisor of m and n
    """
    # Ensure we're working with the smaller number as the divisor initially
    # This is an optimization, but we keep it explicit
    current_dividend = m
    current_divisor = n

    # The Euclidean algorithm: gcd(a, b) = gcd(b, a mod b)
    # We repeat until the remainder becomes 0
    while current_divisor != 0:
        remainder = current_dividend % current_divisor
        current_dividend = current_divisor
        current_divisor = remainder

    # When the loop exits, current_dividend holds the GCD
    return current_dividend

def gcd(a: Number, b: Number) -> int:
    """
    Compute the Greatest Common Divisor (GCD) of two positive integers.

    This function uses the Euclidean algorithm to find the GCD.
    It includes comprehensive input validation and handles all edge cases.

    Args:
        a: First positive integer
        b: Second positive integer

    Returns:
        The greatest common divisor of a and b

    Raises:
        ValueError: If either input is not a positive integer
    """
    # Step 1: Validate inputs explicitly
    valid_a, valid_b = validate_inputs(a, b)

    # Step 2: Handle invalid inputs
    if valid_a is None or valid_b is None:
        raise ValueError(
            "Both inputs must be positive integers (greater than 0). "
            f"Received: a={a}, b={b}"
        )

    # Step 3: Compute GCD using the helper function
    result = gcd_helper(valid_a, valid_b)

    # Step 4: Return the result
    return result