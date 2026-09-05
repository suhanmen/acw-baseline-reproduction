def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
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

    def _validate_input(value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f"Expected integer input, got {type(value).__name__} instead")
        if value < 0:
            raise ValueError(f"Negative input not allowed: {value}. Expected non-negative integer.")

    def _compute_fibfib_iterative(n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 0
        if n == 2:
            return 1

        prev_3 = 0  # Represents fibfib(n-3), initially fibfib(0)
        prev_2 = 0  # Represents fibfib(n-2), initially fibfib(1)
        prev_1 = 1  # Represents fibfib(n-1), initially fibfib(2)

        current = 0
        # We start computing from index 3 up to n
        for _ in range(3, n + 1):
            current = prev_1 + prev_2 + prev_3
            # Shift window: 
            # new prev_3 becomes old prev_2
            # new prev_2 becomes old prev_1
            # new prev_1 becomes current
            prev_3 = prev_2
            prev_2 = prev_1
            prev_1 = current

        return current

    _validate_input(n)
    return _compute_fibfib_iterative(n)