import math

def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Input Validation
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, received {type(n).__name__}")

    if n <= 1:
        raise ValueError("Input must be an integer greater than 1.")

    # We will use a variable to keep track of the current value as we 
    # divide out factors.
    remaining_value = n
    largest_factor = 1

    # Step 1: Handle the smallest prime number (2) separately to allow
    # us to skip even numbers in the subsequent loop.
    if remaining_value % 2 == 0:
        largest_factor = 2
        while remaining_value % 2 == 0:
            remaining_value //= 2

    # Step 2: Check odd numbers starting from 3.
    # We only need to check up to the square root of the current remaining_value.
    # As remaining_value decreases, the upper bound also decreases.
    divisor = 3
    while divisor * divisor <= remaining_value:
        if remaining_value % divisor == 0:
            # If divisor divides remaining_value, it is a prime factor
            # because we are checking from smallest to largest.
            largest_factor = divisor

            # Divide out all occurrences of this prime factor
            while remaining_value % divisor == 0:
                remaining_value //= divisor

        # Increment by 2 to skip even numbers
        divisor += 2

    # Step 3: Final Check
    # If after the loop remaining_value is greater than 1, 
    # it means the remaining_value is itself a prime number 
    # and is the largest prime factor of the original n.
    if remaining_value > 1:
        largest_factor = remaining_value

    return largest_factor