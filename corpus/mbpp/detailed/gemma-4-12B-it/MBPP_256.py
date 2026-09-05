import math
from typing import List

def is_prime(n: int) -> bool:
    """
    Determines if a non-negative integer is a prime number.
    A prime number is a natural number greater than 1 that has no 
    positive divisors other than 1 and itself.
    """
    # Numbers less than 2 are not prime.
    if n < 2:
        return False

    # 2 and 3 are prime.
    if n == 2 or n == 3:
        return True

    # Even numbers greater than 2 and multiples of 3 are not prime.
    if n % 2 == 0 or n % 3 == 0:
        return False

    # A number is prime if it is not divisible by any integer 
    # from 5 up to the square root of n.
    # We check 6k +/- 1 pattern to skip even numbers and multiples of 3.
    limit = int(math.isqrt(n))
    current_divisor = 5
    while current_divisor <= limit:
        if n % current_divisor == 0:
            return False
        if n % (current_divisor + 2) == 0:
            return False
        current_divisor += 6

    return True

def count_Primes_nums(n: int) -> int:
    """
    Counts the number of prime numbers strictly less than a given non-negative integer n.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The count of prime numbers in the range [0, n).

    Raises:
        ValueError: If the input n is a negative integer.
    """
    # Validate input: n must be a non-negative integer.
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")

    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    # Handle edge cases where no primes exist (n <= 2).
    # Primes start at 2, so if n is 0, 1, or 2, the count is 0.
    if n <= 2:
        return 0

    # Use the Sieve of Eratosthenes for efficiency when n is large.
    # The Sieve is much faster than checking each number individually.
    # We create a boolean array representing numbers from 0 to n-1.
    # True means the index is prime, False means it is composite.
    is_prime_sieve = [True] * n

    # 0 and 1 are not prime.
    if n > 0:
        is_prime_sieve[0] = False
    if n > 1:
        is_prime_sieve[1] = False

    # The sieve logic:
    # We only need to iterate up to the square root of n-1.
    limit = int(math.isqrt(n - 1))

    for current_num in range(2, limit + 1):
        # If is_prime_sieve[current_num] is still True, it is prime.
        if is_prime_sieve[current_num]:
            # Mark all multiples of this prime as False (not prime).
            # We start marking from current_num^2 because smaller multiples
            # have already been marked by smaller primes.
            start_multiple = current_num * current_num
            for multiple in range(start_multiple, n, current_num):
                is_prime_sieve[multiple] = False

    # Count how many numbers were left marked as True.
    prime_count = 0
    for i in range(n):
        if is_prime_sieve[i]:
            prime_count += 1

    return prime_count