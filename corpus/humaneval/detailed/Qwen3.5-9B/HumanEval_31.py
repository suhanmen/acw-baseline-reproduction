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

    def _is_valid_integer(candidate):
        """Check if the candidate is a valid integer (excluding booleans).

        Booleans are instances of int in Python, so we explicitly exclude them.
        """
        if not isinstance(candidate, int):
            return False
        if isinstance(candidate, bool):
            return False
        return True

    def _has_no_remainder(dividend, divisor):
        """Check if dividend is divisible by divisor with no remainder.

        Returns True if dividend % divisor == 0, else False.
        """
        return dividend % divisor == 0

    # Step 1: Validate input type
    if not _is_valid_integer(n):
        raise TypeError(f"Expected an integer, but got {type(n).__name__}")

    # Step 2: Handle negative numbers and zero
    # Primes are defined as natural numbers greater than 1
    if n <= 1:
        return False

    # Step 3: Handle the case of 2 (the only even prime)
    if n == 2:
        return True

    # Step 4: Exclude all other even numbers immediately
    if n % 2 == 0:
        return False

    # Step 5: Define the upper bound for trial division
    # We only need to check up to the square root of n
    import math
    limit = int(math.sqrt(n))

    # Step 6: Check for odd divisors from 3 up to the limit
    # We iterate by 2 to skip even numbers (since we already handled divisibility by 2)
    divisor = 3
    is_prime_candidate = True

    while divisor <= limit:
        if _has_no_remainder(n, divisor):
            is_prime_candidate = False
            break

        divisor += 2

    return is_prime_candidate