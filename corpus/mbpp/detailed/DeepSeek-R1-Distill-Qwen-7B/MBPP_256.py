import math

def count_primes_less_than(n):
    """Count the number of prime numbers less than a given non-negative number n."""
    if n <= 2:
        return 0

    def is_prime(number):
        """Check if a number is a prime number."""
        if number <= 1:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(number)) + 1, 2):
            if number % i == 0:
                return False
        return True

    prime_count = 0
    for number in range(2, n):
        if is_prime(number):
            prime_count += 1

    return prime_count