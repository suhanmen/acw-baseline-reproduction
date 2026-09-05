import math
from typing import Optional

def _is_prime_candidate(n: int) -> bool:
    """
    Determine whether a single integer 'n' is a prime number.

    This function handles edge cases explicitly:
    - Numbers less than 2 are not prime.
    - Even numbers greater than 2 are not prime.
    - It checks divisibility only up to the square root of 'n' using a loop.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if 'n' is prime, False otherwise.
    """
    # Edge case: Numbers less than 2 are not prime
    if n < 2:
        return False

    # Edge case: 2 is the only even prime number
    if n == 2:
        return True

    # Edge case: All other even numbers are not prime
    if n % 2 == 0:
        return False

    # Optimization: Check odd divisors up to the square root of n
    # We start checking from 3 and increment by 2.
    limit = int(math.isqrt(n))

    for divisor in range(3, limit + 1, 2):
        if n % divisor == 0:
            return False

    return True


def _get_primes_up_to_limit(limit_exclusive: int) -> list:
    """
    Generate a list of all prime numbers strictly less than the given limit.

    This function iterates from 2 up to limit_exclusive - 1,
    checks each number for primality using _is_prime_candidate,
    and collects the primes into a list.

    Args:
        limit_exclusive (int): The upper bound (exclusive) for the search.

    Returns:
        list: A list of prime numbers less than limit_exclusive.
    """
    if limit_exclusive <= 0:
        return []

    prime_list = []
    # Start checking from 2 up to limit_exclusive - 1
    for number in range(2, limit_exclusive):
        if _is_prime_candidate(number):
            prime_list.append(number)

    return prime_list


def count_Primes_nums(number: int) -> int:
    """
    Count the number of prime numbers less than a given non-negative number.

    This function validates the input, ensures it is an integer,
    checks for non-negative values, and then computes the count
    of prime numbers strictly less than the input.

    Args:
        number (int): The non-negative integer limit. Primes must be strictly less than this value.

    Returns:
        int: The count of prime numbers less than 'number'.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is negative.
    """
    # Validate input type
    if not isinstance(number, int):
        raise TypeError(f"Input must be an integer, got {type(number).__name__}")

    # Validate input range (non-negative)
    if number < 0:
        raise ValueError(f"Input must be non-negative, got {number}")

    # Handle the degenerate case where number is 0 or 1 explicitly for clarity
    # Even though the loop below would handle it, this makes the logic explicit.
    if number <= 1:
        return 0

    # Get the list of primes and return the length of the list
    # This approach is explicit and easier to debug than summing boolean results.
    primes_list = _get_primes_up_to_limit(number)
    return len(primes_list)