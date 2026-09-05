import math

def is_prime(n: int) -> bool:
    """
    Helper function to determine if a number is prime.

    Args:
        n: The integer to check.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    # Prime numbers must be greater than 1
    if n <= 1:
        return False
    # 2 and 3 are prime
    if n <= 3:
        return True
    # Eliminate multiples of 2 and 3 quickly
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check divisors up to the square root of n
    # All primes > 3 are of the form 6k +/- 1
    limit = int(math.isqrt(n))
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True

def max_Prime_Factors(n: int) -> int:
    """
    Finds the largest prime factor of a given integer n.

    Args:
        n: The integer to analyze.

    Returns:
        int: The largest prime factor of n.

    Raises:
        ValueError: If the input is less than 2.
    """
    # Input Validation
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")

    if n < 2:
        # The smallest prime number is 2. 
        # Prime factorization is defined for integers >= 2.
        raise ValueError("Input must be an integer greater than or equal to 2.")

    # Handle the case of a single prime number or small numbers
    # We use a copy of n to perform reductions
    remaining_n = n
    largest_factor = 1

    # Extract all factors of 2
    if remaining_n % 2 == 0:
        largest_factor = 2
        while remaining_n % 2 == 0:
            remaining_n //= 2

    # Extract factors of 3
    if remaining_n % 3 == 0:
        largest_factor = 3
        while remaining_n % 3 == 0:
            remaining_n //= 3

    # Extract odd factors starting from 5
    # We only need to check up to the square root of the remaining number
    # because a number can have at most one prime factor greater than its square root.
    d = 5
    while d * d <= remaining_n:
        # Check for 6k - 1
        if remaining_n % d == 0:
            largest_factor = d
            while remaining_n % d == 0:
                remaining_n //= d

        # Check for 6k + 1
        d_plus_2 = d + 2
        if remaining_n % d_plus_2 == 0:
            largest_factor = d_plus_2
            while remaining_n % d_plus_2 == 0:
                remaining_n //= d_plus_2

        # Increment by 6 to maintain 6k +/- 1 pattern
        d += 6

    # If remaining_n is still greater than 1, then the remaining 
    # part of the number is itself a prime number and is the largest factor.
    if remaining_n > 1:
        largest_factor = remaining_n

    return largest_factor