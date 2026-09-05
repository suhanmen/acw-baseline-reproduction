import math
from typing import Optional


def _is_prime(candidate: int) -> bool:
    """
    Determine if a given integer is a prime number.

    This function handles edge cases explicitly:
    - Numbers less than 2 are not prime.
    - 2 and 3 are prime.
    - Even numbers greater than 2 are not prime.
    - For odd numbers greater than 3, it checks divisibility up to the square root.

    Args:
        candidate: The integer to check for primality.

    Returns:
        True if candidate is prime, False otherwise.
    """
    if candidate < 2:
        return False
    if candidate == 2 or candidate == 3:
        return True
    if candidate % 2 == 0:
        return False

    limit = int(math.isqrt(candidate))
    divisor = 3
    while divisor <= limit:
        if candidate % divisor == 0:
            return False
        divisor += 2
    return True


def _get_prime_factors(number: int) -> list[int]:
    """
    Find all prime factors of a given number.

    This function uses trial division to find factors.
    It starts with 2, then proceeds with odd numbers up to sqrt(number).
    If after this process the number is greater than 1, the remaining number
    is itself a prime factor.

    Args:
        number: The integer to factorize (must be > 1).

    Returns:
        A list of prime factors in non-decreasing order.
    """
    factors = []
    n = number

    # Handle factor of 2
    if n % 2 == 0:
        # Add 2 as many times as it divides n
        factors.append(2)
        while n % 2 == 0:
            n = n // 2

    # Handle odd factors starting from 3
    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        divisor += 2

    # If n is still greater than 1, then the remaining n is a prime number
    if n > 1:
        factors.append(n)

    return factors


def _find_largest_prime_factor_via_factors(number: int) -> Optional[int]:
    """
    Find the largest prime factor by generating all prime factors first.

    This approach is straightforward and educational, though not the most
    efficient for extremely large numbers. It ensures we get all factors
    and can easily determine the maximum.

    Args:
        number: The integer to analyze (must be > 1).

    Returns:
        The largest prime factor if found, None otherwise.
    """
    if number <= 1:
        return None

    factors = _get_prime_factors(number)

    if not factors:
        return None

    return max(factors)


def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.

    This function implements a robust solution to find the largest prime factor.
    It includes comprehensive input validation and handles edge cases explicitly.

    While the problem statement assumes n > 1 and is not a prime, this implementation
    includes defensive checks to provide meaningful error messages or handled behavior
    for invalid inputs in production contexts.

    Args:
        n: The integer to find the largest prime factor for.

    Returns:
        The largest prime factor of n.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is not greater than 1.

    Examples:
        >>> largest_prime_factor(13195)
        29
        >>> largest_prime_factor(2048)
        2
        >>> largest_prime_factor(600851475143)
        6857
    """
    # Step 1: Type validation
    # Ensure n is an integer instance (excluding bool which is a subclass of int)
    if not isinstance(n, int):
        raise TypeError(f"Expected integer input, got {type(n).__name__}")

    # Step 2: Boolean validation
    # Explicitly reject boolean values as they are instances of int in Python
    if isinstance(n, bool):
        raise TypeError("Boolean values are not accepted as input. Use True/False instead of 1/0.")

    # Step 3: Domain validation
    # The problem states n > 1. We enforce this strictly.
    if n <= 1:
        raise ValueError(f"Input must be greater than 1, got {n}.")

    # Step 4: Handle potential overflow or extremely large numbers gracefully
    # Python handles arbitrarily large integers, but we want to ensure
    # our algorithm doesn't hang on pathological inputs if we could detect them.
    # For this problem, we assume reasonable computational resources.

    # Step 5: Find the largest prime factor
    # We use the helper function that generates all factors first
    largest_factor = _find_largest_prime_factor_via_factors(n)

    # Step 6: Final validation of the result
    if largest_factor is None:
        # This should theoretically not happen given the problem constraints (n > 1)
        raise RuntimeError(f"Failed to find any prime factor for {n}. This indicates an unexpected error in the factorization logic.")

    return largest_factor