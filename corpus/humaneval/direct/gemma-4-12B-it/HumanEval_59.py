def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    d = 2
    while d * d <= n:
        if n % d == 0:
            n //= d
        else:
            d += 1
    return n