from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    # Initialize the list to store prime factors
    factors: List[int] = []

    # Handle edge case where the input number is 1
    # 1 is not a prime number and has no prime factors
    if n == 1:
        return factors

    # Handle edge case where the input number is less than 1
    # Prime factorization is typically defined for positive integers greater than 1.
    # Negative numbers and zero do not have a standard prime factorization in this context.
    if n < 1:
        raise ValueError("Prime factorization is only defined for positive integers greater than 1.")

    # Handle the edge case where n is 0
    if n == 0:
        raise ValueError("Prime factorization is undefined for zero.")

    # Factor out 2 separately to allow incrementing by 2 in the main loop
    # This optimizes the process by handling even numbers first.
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    # Initialize the divisor to check for odd factors
    divisor: int = 3

    # Check for odd factors starting from 3 up to the square root of n
    # We only need to go up to sqrt(n) because if n has a factor greater than sqrt(n),
    # the corresponding co-factor must be less than sqrt(n) and would have been found already.
    while divisor * divisor <= n:
        # Check if the current divisor divides n
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        # Increment the divisor by 2 to check only odd numbers
        divisor += 2

    # If n is still greater than 1 after checking all factors up to sqrt(n),
    # then the remaining n is a prime number itself.
    if n > 1:
        factors.append(n)

    return factors