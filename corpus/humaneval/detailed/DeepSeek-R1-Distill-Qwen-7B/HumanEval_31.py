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

    # Handle numbers less than 2 and negative numbers
    if n <= 1 or n < 0:
        return False

    # Check if n is 2 (the smallest prime)
    if n == 2:
        return True

    # Check if n is even
    if n % 2 == 0:
        return False

    # Calculate the square root of n for the loop limit
    sqrt_n = n ** 0.5

    # Check for factors from 3 up to sqrt(n)
    for i in range(3, int(sqrt_n) + 1, 2):
        if n % i == 0:
            return False

    # If no factors found, n is prime
    return True