def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """

    # Validate input
    if not isinstance(n, int) or n < 0:
        return []

    # Handle edge cases
    if n == 0 or n == 1:
        return []

    # List to hold the primes found
    primes = []

    # Check numbers starting from 2 up to n-1 for being prime and add to primes
    for number in range(2, n):
        if is_prime(number):
            primes.append(number)
            if len(primes) == n:
                break

    return primes

def is_prime(num):
    """Helper function to check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True