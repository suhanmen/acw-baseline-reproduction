def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.

    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Handle the case of even numbers first
    while n % 2 == 0:
        max_prime = 2
        n = n // 2

    # Now n must be odd; start checking from 3 onwards
    max_prime = 2
    current = 3
    while current * current <= n:
        while n % current == 0:
            max_prime = current
            n = n // current
        current += 2

    # If remaining n is a prime number greater than 2
    if n > 2:
        max_prime = n

    return max_prime