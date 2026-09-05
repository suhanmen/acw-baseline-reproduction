def fib(n: int):
    """Return n-th Fibonacci number.

    Raises:
        ValueError: If n is not a positive integer.
    """
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    if n < 0:
        raise ValueError("n cannot be negative")

    if n == 0:
        raise ValueError("n cannot be zero")
    elif n == 1:
        return 1
    elif n == 2:
        return 1

    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b