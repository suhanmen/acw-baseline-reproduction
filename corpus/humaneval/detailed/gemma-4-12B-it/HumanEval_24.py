import math

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Input validation: ensure n is an integer
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, received {type(n).__name__}")

    # Handle values less than 2. 
    # By definition, divisors are typically positive integers.
    # A number smaller than 2 does not have a positive divisor smaller than itself.
    if n < 2:
        # Depending on requirements, we could raise a ValueError or return 0.
        # Given the context of divisors, numbers < 2 do not have a "largest divisor smaller than n"
        # in the sense of natural numbers.
        raise ValueError("Input must be an integer greater than 1 to have a smaller divisor.")

    # We are looking for the largest divisor d such that d < n.
    # This is equivalent to finding the smallest divisor k such that k > 1.
    # Then, the largest divisor is n / k.
    # Example: n = 15. Smallest divisor > 1 is 3. Largest divisor < 15 is 15 / 3 = 5.
    # Example: n = 16. Smallest divisor > 1 is 2. Largest divisor < 16 is 16 / 2 = 8.

    # We search for the smallest factor starting from 2 up to sqrt(n).
    smallest_factor = find_smallest_factor(n)

    if smallest_factor is None:
        # If no factor is found up to sqrt(n), the number is prime.
        # The largest divisor smaller than a prime number is 1.
        return 1
    else:
        # If a factor was found, the largest divisor is n divided by that factor.
        result = n // smallest_factor
        return result

def find_smallest_factor(number: int) -> int:
    """
    Finds the smallest integer factor of 'number' greater than 1.
    Returns None if the number is prime.
    """
    # Start checking from the smallest prime.
    # We only need to check up to the square root of the number.
    limit = int(math.isqrt(number))

    for i in range(2, limit + 1):
        if number % i == 0:
            return i

    return None