import math
from typing import Union

def _validate_input(n: object) -> int:
    """
    Validates that the input is a non-negative integer.

    Args:
        n: The input value to validate.

    Returns:
        The validated integer n.

    Raises:
        TypeError: If n is not an integer (bool is a subclass of int, so we reject it).
        ValueError: If n is negative.
    """
    # Check if the type is exactly int. 
    # We explicitly check for bool because bool is a subclass of int in Python.
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"Input must be an integer, got {type(n).__name__}")

    if n < 0:
        raise ValueError(f"Input must be a non-negative integer, got {n}")

    return n

def _compute_standard_factorial(value: int) -> int:
    """
    Computes the standard factorial of a non-negative integer.

    Args:
        value: A non-negative integer.

    Returns:
        The factorial of value (value!).
    """
    if value < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(value)

def _compute_brazilian_factorial(n: int) -> int:
    """
    Computes the Brazilian factorial for a non-negative integer n.

    Definition: brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    Note: The mathematical definition implies n > 0. 
    However, mathematically 0! = 1, and the product from 0! to 0! is just 1.
    Based on the problem statement "n > 0", we handle n=0 as a boundary case 
    that results in 1 (product of an empty sequence conceptually or just 0!).

    Args:
        n: A non-negative integer.

    Returns:
        The computed Brazilian factorial.
    """
    if n < 0:
        raise ValueError("Brazilian factorial is not defined for negative numbers.")

    total_product: int = 1

    # We iterate from 1 up to n to calculate the product of factorials.
    # The terms are: n!, (n-1)!, ..., 1!
    # We can iterate i from 1 to n (inclusive) and multiply by i!
    # This covers 1!, 2!, ..., n!.

    for current_number in range(1, n + 1):
        current_factorial: int = _compute_standard_factorial(current_number)
        total_product *= current_factorial

    return total_product

def special_factorial(n: object) -> int:
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    # Step 1: Validate the input explicitly.
    validated_n: int = _validate_input(n)

    # Step 2: Compute the Brazilian factorial using the validated integer.
    result: int = _compute_brazilian_factorial(validated_n)

    return result