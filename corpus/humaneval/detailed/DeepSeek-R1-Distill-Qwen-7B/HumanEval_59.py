def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n <= 1:
        return 0  # No prime factors for n <= 1

    # Check if n is a prime number (though problem says it's not, as a safeguard)
    if n == 2:
        return 2
    if n % 2 == 0:
        return 2  # 2 is the largest prime factor if n is even

    largest_factor = 1
    # Remove all factors of 2
    while n % 2 == 0:
        largest_factor = 2
        n //= 2

    # Now n must be odd. Start checking odd numbers from 3 upwards
    i = 3
    max_factor = (n ** 0.5)  # Only check up to sqrt(n) for efficiency
    while i <= max_factor and n > 1:
        while n % i == 0:
            largest_factor = i
            n //= i
            max_factor = (n ** 0.5)  # Update sqrt after division
        i += 2  # Check only odd numbers

    # If remaining n is a prime number greater than 2
    if n > 2:
        largest_factor = n

    return largest_factor