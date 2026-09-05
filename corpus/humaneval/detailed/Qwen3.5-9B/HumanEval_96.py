import math
from typing import List, Union

def is_even(value: int) -> bool:
    """Check if a number is even."""
    return value % 2 == 0

def is_divisible_by(num_to_check: int, divisor: int) -> bool:
    """Check if num_to_check is divisible by divisor (divisor > 1)."""
    return num_to_check % divisor == 0

def check_prime(number: int) -> bool:
    """
    Determine if a given number is prime.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    This function uses trial division up to the square root of the number.

    Args:
        number: The integer to check.

    Returns:
        True if the number is prime, False otherwise.
    """
    # 0, 1, and 2 are special cases
    if number < 2:
        return False

    if number == 2:
        return True

    if number == 3:
        return True

    # Even numbers greater than 2 are not prime
    if is_even(number):
        return False

    # Check for odd factors up to the square root of number
    # We start at 3 and increment by 2 to only check odd numbers
    limit = int(math.isqrt(number)) + 1

    for divisor in range(3, limit, 2):
        if is_divisible_by(number, divisor):
            return False

    return True

def generate_primes_less_than(limit: int) -> List[int]:
    """
    Generate a list of all prime numbers strictly less than the given limit.

    Args:
        limit: The upper bound (exclusive) for prime numbers.

    Returns:
        A list of prime numbers less than limit.
    """
    primes = []

    # Handle small limits explicitly
    if limit <= 2:
        return primes

    # 2 is the first prime
    if limit > 2:
        primes.append(2)

    # Check only odd numbers starting from 3 up to limit
    # We stop before limit because the requirement is "less than n"
    for candidate in range(3, limit, 2):
        if check_prime(candidate):
            primes.append(candidate)

    return primes

def count_up_to(n: Union[int, float]) -> List[int]:
    """
    Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.

    Note: Despite the docstring saying "first n integers", the examples clearly indicate
    that the function should return ALL prime numbers less than n.
    For instance, count_up_to(5) returns [2, 3], which are all primes < 5.
    If it meant "first 5 primes", the result would be [2, 3, 5, 7, 11].
    The examples confirm the requirement is "all primes less than n".

    Args:
        n: A number representing the upper bound (exclusive).

    Returns:
        A list of prime numbers strictly less than n.

    Raises:
        TypeError: If n is not an integer or is negative.
        ValueError: If n is not an integer (e.g., float).
    """

    # Step 1: Validate the input type
    if not isinstance(n, int):
        raise TypeError(f"Expected an integer input, but got {type(n).__name__}.")

    # Step 2: Validate the input value
    if n < 0:
        raise ValueError(f"Input must be a non-negative integer, but got {n}.")

    # Step 3: Generate the list of primes less than n using our helper function
    primes_list = generate_primes_less_than(n)

    # Step 4: Return the result
    return primes_list