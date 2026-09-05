import math

def is_prime(num: int) -> bool:
    """
    Helper function to determine if a non-negative integer is a prime number.
    A prime number is a natural number greater than 1 that has no positive 
    divisors other than 1 and itself.
    """
    # Numbers less than 2 are not prime
    if num < 2:
        return False

    # 2 is the only even prime number
    if num == 2:
        return True

    # Eliminate all other even numbers immediately
    if num % 2 == 0:
        return False

    # Check for divisors from 3 up to the square root of num
    # We skip even numbers by using a step of 2 in the range
    limit = int(math.isqrt(num))
    for divisor in range(3, limit + 1, 2):
        if num % divisor == 0:
            return False

    return True

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
    # Validate input: ensure n is an integer
    if not isinstance(n, int):
        raise ValueError("Input n must be an integer.")

    # Handle negative numbers: technically non-negative was requested, 
    # but we handle negative to be defensive.
    if n < 0:
        return []

    # Initialize the list to store prime numbers
    primes_list = []

    # Iterate through every integer starting from 2 (the first prime)
    # up to (but not including) n.
    for current_number in range(2, n):
        # Check if the current number is prime using our helper
        is_currently_prime = is_prime(current_number)

        # If it is prime, add it to our results list
        if is_currently_prime:
            primes_list.append(current_number)

    return primes_list