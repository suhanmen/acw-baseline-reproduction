import math

def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    # Validate input type
    # Prime numbers are by definition integers.
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, but received {type(n).__name__}")

    # Handle numbers less than 2
    # 0 and 1 are not prime. Negative numbers are not prime.
    if n < 2:
        return False

    # Handle the only even prime number
    if n == 2:
        return True

    # Handle all other even numbers
    if n % 2 == 0:
        return False

    # Check for primality by testing divisors
    # We only need to check up to the square root of n.
    # If n has a factor greater than its square root, it must have 
    # a corresponding factor smaller than its square root.
    limit = int(math.isqrt(n))

    # We start from 3 and check only odd numbers.
    # Step size is 2 to skip even numbers.
    current_divisor = 3
    while current_divisor <= limit:
        if n % current_divisor == 0:
            # If n is divisible by any number other than 1 and itself,
            # it is composite.
            return False
        current_divisor += 2

    # If no divisors were found in the loop, the number is prime.
    return True