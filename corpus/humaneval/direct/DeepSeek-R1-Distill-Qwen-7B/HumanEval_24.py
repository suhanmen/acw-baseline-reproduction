def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n

    >>> largest_divisor(15)
    5
    """
    if n == 1:
        return None  # 1 has no divisors smaller than itself

    # Start from the square root of n and move downwards to find the largest divisor
    for i in range(int(n**0.5), 1, -1):
        if n % i == 0:
            return n // i

    # If no divisor found, n is prime and its largest divisor is 1
    return 1