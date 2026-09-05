def prime_fib(n: int):
    """
    prime_fib returns the n-th number that is both a Fibonacci number and a prime number.

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
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    fibonacci = [0, 1]
    while len(fibonacci) < n:
        next_num = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_num)
        if is_prime(next_num):
            pass  # We collect them in a separate list
    primes = []
    for num in fibonacci[2:]:  # Start from 2, since 0 and 1 are not considered
        if is_prime(num):
            primes.append(num)
            if len(primes) == n:
                return primes[-1]
    return primes[n-1]