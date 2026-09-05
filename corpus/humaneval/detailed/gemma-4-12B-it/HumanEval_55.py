import typing

def fib(n: int) -> int:
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # Validate input type
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, received {type(n).__name__}")

    # Handle negative inputs: Fibonacci sequence index is usually non-negative
    if n < 0:
        raise ValueError("Fibonacci index cannot be negative.")

    # Handle the base cases for the Fibonacci sequence
    # Standard definition: F(0) = 0, F(1) = 1, F(2) = 1, F(3) = 2...
    # Based on the docstring examples:
    # fib(1) = 1
    # fib(8) = 21
    # This implies F(0) = 0, F(1) = 1, F(2) = 1, F(3) = 2, F(4) = 3, 
    # F(5) = 5, F(6) = 8, F(7) = 13, F(8) = 21, F(9) = 34, F(10) = 55.

    if n == 0:
        return 0

    if n == 1:
        return 1

    # Iterative approach to calculate Fibonacci numbers
    # This is O(n) time complexity and O(1) space complexity.
    # We use iteration instead of recursion to avoid RecursionError for large n.

    previous_value: int = 0  # Represents F(i-2)
    current_value: int = 1    # Represents F(i-1)

    # We start calculating from index 2 up to n inclusive
    for _ in range(2, n + 1):
        # The next number is the sum of the previous two
        next_value: int = previous_value + current_value

        # Shift values forward for the next iteration
        previous_value = current_value
        current_value = next_value

    return current_value