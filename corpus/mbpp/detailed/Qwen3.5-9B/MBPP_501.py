from math import gcd
from typing import Tuple, Union

Number = Union[int, float]

def _validate_number(value: Number) -> None:
    """
    Validates that the provided input is a numeric type (int or float).
    Raises a TypeError if the validation fails.
    """
    if not isinstance(value, (int, float)):
        raise TypeError(f"Expected an integer or float, but got {type(value).__name__}")

def _normalize_to_int(value: Number) -> int:
    """
    Converts a numeric input to an integer.
    Raises a ValueError if the input is a float with a non-zero fractional part.
    """
    if isinstance(value, float):
        if not value.is_integer():
            raise ValueError(f"Float values must have a zero fractional part: {value}")
    return int(value)

def _handle_zero_case(n1: int, n2: int) -> int:
    """
    Handles the specific case where one or both numbers are zero.
    Returns 0 if both are zero (undefined, but treated as no common divisor).
    Returns the non-zero number if only one is zero.
    Raises ValueError if both are zero.
    """
    if n1 == 0 and n2 == 0:
        raise ValueError("Common divisor is undefined for the pair (0, 0).")
    if n1 == 0:
        return abs(n2)
    if n2 == 0:
        return abs(n1)
    return _compute_common_divisor_for_non_zero(n1, n2)

def _compute_common_divisor_for_non_zero(n1: int, n2: int) -> int:
    """
    Computes the greatest common divisor (GCD) for two non-zero integers.
    Uses the absolute values because divisors are typically considered positive.
    """
    abs_n1 = abs(n1)
    abs_n2 = abs(n2)
    result = gcd(abs_n1, abs_n2)
    return result

def num_comm_div(n1: Number, n2: Number) -> int:
    """
    Finds the greatest common divisor (GCD) between two numbers in a given pair.

    This function handles various edge cases including:
    - Empty input (handled via type validation)
    - Single element (conceptually not applicable to a pair, but handled per element)
    - All-equal elements (returns the absolute value of the element)
    - Boundary values (0, 1, -1)
    - Zero and negative numbers

    The 'common divisor' in this context is interpreted as the Greatest Common Divisor (GCD).
    The problem examples (2,4)->2, (12,24)->6 confirm this interpretation (GCD).

    Args:
        n1: The first number in the pair.
        n2: The second number in the pair.

    Returns:
        The greatest common divisor of the two numbers as an integer.

    Raises:
        TypeError: If either input is not a number (int or float).
        ValueError: If both inputs are zero (undefined GCD) or if a float has a fractional part.
    """
    # Step 1: Validate inputs are numbers
    _validate_number(n1)
    _validate_number(n2)

    # Step 2: Normalize inputs to integers
    try:
        int_n1 = _normalize_to_int(n1)
        int_n2 = _normalize_to_int(n2)
    except ValueError as e:
        raise ValueError(f"Invalid number format: {e}")

    # Step 3: Handle zero cases explicitly
    if int_n1 == 0 or int_n2 == 0:
        return _handle_zero_case(int_n1, int_n2)

    # Step 4: Compute GCD for non-zero integers
    return _compute_common_divisor_for_non_zero(int_n1, int_n2)