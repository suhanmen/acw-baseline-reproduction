def prime_fib(n: int) -> int:
    """
    prime_fib returns the n-th number that is both a Fibonacci number and a prime number.

    Args:
        n: The position in the sequence of prime Fibonacci numbers to return.

    Returns:
        The n-th prime Fibonacci number.

    Raises:
        ValueError: If n is not a positive integer.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")

    def is_prime(num: int) -> bool:
        """Check if a number is prime."""
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= num:
            if num % i == 0:
                return False
            i += w
            w = 6 - w
        return True

    a, b = 0, 1
    count = 0
    while True:
        if is_prime(a):
            count += 1
            if count == n:
                return a
        a, b = b, a + b
        # Prevent infinite loop in case no prime Fibonacci numbers exist beyond a certain point
        if a > 10**18:  # Arbitrarily large number to prevent infinite loop
            break