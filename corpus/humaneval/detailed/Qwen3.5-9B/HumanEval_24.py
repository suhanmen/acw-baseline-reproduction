from typing import Optional


def _is_valid_integer_input(value: object) -> bool:
    """
    Validate that the input is exactly an integer (excluding booleans).

    Args:
        value: The value to validate.

    Returns:
        True if the value is an integer (and not a bool), False otherwise.
    """
    if not isinstance(value, int):
        return False
    if isinstance(value, bool):
        return False
    return True


def _is_positive_integer(value: int) -> bool:
    """
    Check if the value is a positive integer (greater than 0).

    Args:
        value: The integer to check.

    Returns:
        True if value > 0, False otherwise.
    """
    return value > 0


def _find_largest_proper_divisor(n: int) -> int:
    """
    Find the largest divisor of n that is strictly less than n.

    This function assumes n is a positive integer greater than 1.
    If n is prime, it returns 1. If n is composite, it returns the largest factor < n.
    For n=2, it returns 1.

    Algorithm:
    Iterate from sqrt(n) down to 1. The first divisor found will be the 
    largest divisor <= sqrt(n). The corresponding co-divisor (n / divisor) 
    will be the largest proper divisor of n.
    If no divisor is found in that range (n is prime), return 1.

    Args:
        n: A positive integer greater than 1.

    Returns:
        The largest divisor of n strictly less than n.
    """
    import math

    # Calculate the integer square root of n
    sqrt_n = int(math.isqrt(n))

    # We start searching from the square root downwards to find the largest
    # factor less than or equal to sqrt(n).
    largest_factor_sqrt = 1

    for candidate in range(sqrt_n, 0, -1):
        if n % candidate == 0:
            # We found a factor <= sqrt(n).
            # The corresponding co-factor (n / candidate) is the largest 
            # proper divisor of n.
            largest_factor_sqrt = candidate
            break

    # The largest proper divisor is n divided by the smallest factor >= 2.
    # Since we found the largest factor <= sqrt(n), the co-factor is the answer.
    # However, if n is prime, the loop finishes with largest_factor_sqrt = 1.
    # In that case, the largest proper divisor is still 1.
    # If n is composite, the co-factor is n // largest_factor_sqrt.

    # Edge case handling within the logic:
    # If largest_factor_sqrt remains 1, it means n is prime (or n=1, but n>1 here).
    # For prime numbers, the largest proper divisor is 1.
    # For composite numbers, n // largest_factor_sqrt gives the largest proper divisor.

    if largest_factor_sqrt == 1:
        # n is prime
        return 1
    else:
        # n is composite. The largest proper divisor is n divided by its smallest prime factor.
        # Our loop found the largest factor <= sqrt(n). 
        # The pair (candidate, n/candidate) sums up to divisors.
        # The largest proper divisor is n // largest_factor_sqrt.
        return n // largest_factor_sqrt


def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    This function handles various edge cases:
    - n <= 1: Raises a ValueError because no proper divisor exists (divisor must be < n and >= 1).
    - Negative numbers: Raises a ValueError.
    - Zero: Raises a ValueError.

    Examples:
        >>> largest_divisor(15)
        5
        >>> largest_divisor(17)  # Prime
        1
        >>> largest_divisor(16)  # Power of 2
        8
        >>> largest_divisor(1)
        Traceback (most recent call last):
        ...
        ValueError: Input must be a positive integer greater than 1.

    Args:
        n: The integer to analyze.

    Returns:
        The largest integer d such that d divides n evenly and d < n.

    Raises:
        TypeError: If n is not an integer or is a boolean.
        ValueError: If n is less than or equal to 1.
    """
    # Step 1: Validate type
    if not _is_valid_integer_input(n):
        raise TypeError(f"Expected an integer, but received {type(n).__name__}.")

    # Step 2: Validate value range
    # The problem requires a divisor smaller than n. 
    # A divisor must be at least 1. Therefore, n must be at least 2.
    if n <= 1:
        raise ValueError(f"Input must be a positive integer greater than 1. Received: {n}")

    # Step 3: Compute the result using the helper function
    result = _find_largest_proper_divisor(n)

    # Step 4: Return the result
    return result