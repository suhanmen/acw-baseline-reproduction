import math

def is_prime(num: int) -> bool:
    """
    Determines if a given integer is a prime number.

    Args:
        num: The integer to check.

    Returns:
        True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    # Optimization: Check divisors up to the square root of num
    # using the 6k +/- 1 rule.
    limit = int(math.isqrt(num))
    for i in range(5, limit + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True

def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    # Input Validation: n must be a positive integer.
    if not isinstance(n, int):
        raise TypeError("The input 'n' must be an integer.")

    if n <= 0:
        raise ValueError("The input 'n' must be a positive integer greater than 0.")

    # State variables for Fibonacci sequence generation
    # The sequence starts 0, 1, 1, 2, 3, 5, 8...
    prev_fib = 0
    curr_fib = 1

    # Counter for how many prime Fibonacci numbers we have found
    prime_count = 0

    # We iterate through Fibonacci numbers until we find the n-th prime one.
    # Since we need the n-th prime Fibonacci, we continue generating 
    # numbers until prime_count reaches n.
    while prime_count < n:
        # Calculate the next Fibonacci number
        next_fib = prev_fib + curr_fib

        # Update pointers to move forward in the sequence
        prev_fib = curr_fib
        curr_fib = next_fib

        # Check if the newly generated Fibonacci number is prime.
        # Note: 0 and 1 are technically Fibonacci numbers but are not prime.
        # The loop starts checking from the third Fibonacci number (1+1=2).
        if is_prime(curr_fib):
            prime_count += 1

            # If this is the n-th one, return it immediately.
            if prime_count == n:
                return curr_fib

    # This line is theoretically unreachable given the logic above,
    # but is kept for completeness of the flow.
    return -1