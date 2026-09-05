from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    # Defensive Programming: Validate input types
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, received: {type(n).__name__}")

    # Handle degenerate cases: 0, 1, and negative numbers.
    # Prime factorization is typically defined for integers > 1.
    # For 1, the product of an empty list is 1.
    # For 0 and negatives, prime factorization is not standard; we raise ValueError.
    if n < 0:
        raise ValueError("Factorization is not defined for negative integers in this context.")
    if n == 0:
        raise ValueError("Factorization is not defined for zero.")
    if n == 1:
        return []

    factors: List[int] = []

    # We start checking from the smallest prime, which is 2.
    # We use a temporary variable to reduce n as we find factors.
    remaining_value: int = n

    # Handle the factor 2 separately to allow us to increment the divisor by 2 later.
    # This is a standard optimization for trial division.
    while remaining_value % 2 == 0:
        factors.append(2)
        remaining_value //= 2

    # Check odd divisors starting from 3.
    # The limit is the square root of the remaining value.
    # As remaining_value decreases, the upper bound also decreases.
    divisor: int = 3
    while divisor * divisor <= remaining_value:
        # While the current divisor divides the remaining value, 
        # it is a prime factor (since smaller factors were already removed).
        while remaining_value % divisor == 0:
            factors.append(divisor)
            remaining_value //= divisor

        # Increment by 2 to skip even numbers.
        divisor += 2

    # If remaining_value is still greater than 1, it must be prime.
    if remaining_value > 1:
        factors.append(remaining_value)

    # The factors are collected in non-decreasing order because we 
    # iterate through divisors from smallest to largest.
    return factors