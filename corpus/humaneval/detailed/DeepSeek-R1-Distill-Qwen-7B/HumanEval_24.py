def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n

    Edge Cases:
    - n < 2: return n itself as it has no proper divisors
    - n <= 0: return n as a way to handle zero and negatives
    - n = 1: return 1 since 1 has no proper divisors

    Steps:
    1. Validate input to handle non-positive numbers, zero, and numbers less than 2.
    2. If the number is 1, return 1.
    3. Start from the largest possible divisor and work downwards to find the proper divisor efficiently.
    4. Use the square root of the number to limit the search range and find the largest proper divisor.
    5. Return the largest proper divisor found.

    >>> largest_divisor(15)
    5
    """
    # Handle edge cases
    if n < 2:
        if n == 1:
            return 1
        else:
            return n  # For n <= 0, we return n itself to avoid division by zero

    # For positive n, find the largest proper divisor
    largest = 1
    sqrt_n = int(n ** 0.5)

    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            # Update largest with the maximum of current divisor and its complement
            largest = max(largest, i, n // i)

    return largest if largest < n else 1