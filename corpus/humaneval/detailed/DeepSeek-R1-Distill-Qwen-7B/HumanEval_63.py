def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.

    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    # Check if input is a valid non-negative integer
    if not isinstance(n, int) or n < 0:
        return None

    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1

    # For n >= 3, use iterative calculation to avoid recursion and stack issues
    a, b, c = 0, 0, 1  # Represents fibfib(0), fibfib(1), fibfib(2)
    for _ in range(3, n + 1):
        next_val = a + b + c
        a, b, c = b, c, next_val

    return c