def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    # Validate input
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")

    # Base cases
    if n == 0 or n == 1 or n == 3:
        return 0
    elif n == 2:
        return 2

    # Initialize the first four values
    a, b, c, d = 0, 0, 2, 0

    # Compute values iteratively up to n
    for _ in range(4, n + 1):
        next_val = a + b + c + d
        a, b, c, d = b, c, d, next_val

    return d if n > 3 else d  # Return the nth value

    # The function is now complete.