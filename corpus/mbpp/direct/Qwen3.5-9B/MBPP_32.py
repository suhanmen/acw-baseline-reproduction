def max_Prime_Factors(n):
    """
    Returns the largest prime factor of a given integer n.
    """
    if n <= 1:
        return n

    largest_prime = -1

    # Remove factors of 2
    while n % 2 == 0:
        largest_prime = 2
        n //= 2

    # Check odd factors up to sqrt(n)
    i = 3
    while i * i <= n:
        while n % i == 0:
            largest_prime = i
            n //= i
        i += 2

    # If n is now greater than 1, it's a prime number itself
    if n > 1:
        largest_prime = n

    return largest_prime