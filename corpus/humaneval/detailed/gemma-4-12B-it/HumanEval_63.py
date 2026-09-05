from typing import List

def fibfib(n: int) -> int:
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
    # Validate input type
    if not isinstance(n, int):
        raise TypeError(f"Input 'n' must be an integer, received {type(n).__name__}")

    # Handle negative indices
    # The sequence is defined for n >= 0. Based on standard Fibonacci-like 
    # behavior, we treat negative inputs as invalid or raise an error.
    if n < 0:
        raise ValueError("The FibFib sequence is not defined for negative integers.")

    # Handle base cases explicitly as defined in the problem description
    # fibfib(0) == 0
    # fibfib(1) == 0
    # fibfib(2) == 1
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1

    # For n > 2, we use an iterative approach to compute the sequence.
    # This is O(n) time complexity and O(1) space complexity.
    # We maintain the last three values to compute the next one.

    # Initial state corresponds to:
    # f(0) = 0
    # f(1) = 0
    # f(2) = 1
    prev_three = 0  # Represents fibfib(i-3)
    prev_two = 0     # Represents fibfib(i-2)
    prev_one = 1     # Represents fibfib(i-1)

    # Current value to store the result
    current_value = 0

    # We start computing from n=3 up to n.
    # Loop range is [3, n+1) to include n.
    for i in range(3, n + 1):
        # Formula: fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
        current_value = prev_one + prev_two + prev_three

        # Shift the window for the next iteration:
        # The old prev_two becomes the new prev_three
        # The old prev_one becomes the new prev_two
        # The current_value becomes the new prev_one
        prev_three = prev_two
        prev_two = prev_one
        prev_one = current_value

    return current_value