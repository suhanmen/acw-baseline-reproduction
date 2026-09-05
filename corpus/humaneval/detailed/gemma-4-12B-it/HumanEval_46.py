def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    # Validate input: Ensure n is an integer
    if not isinstance(n, int):
        raise TypeError(f"Input n must be an integer, but received {type(n).__name__}.")

    # Validate input: Sequence is typically defined for non-negative integers
    if n < 0:
        raise ValueError("Input n must be a non-negative integer.")

    # Handle the base cases explicitly as defined in the problem statement
    # fib4(0) -> 0
    if n == 0:
        return 0

    # fib4(1) -> 0
    if n == 1:
        return 0

    # fib4(2) -> 2
    if n == 2:
        return 2

    # fib4(3) -> 0
    if n == 3:
        return 0

    # For n > 3, we use an iterative approach to calculate the sequence.
    # This avoids the overhead of recursion and keeps space complexity to O(1).

    # Initialize the first four values of the sequence
    # index: 0, 1, 2, 3
    f0 = 0
    f1 = 0
    f2 = 2
    f3 = 0

    # current_val will store the result of fib4(i)
    # We iterate from 4 up to n inclusive.
    # To calculate the next value, we sum the previous four.

    # We use a sliding window approach to keep track of the 4 previous values.
    # prev_values[0] is fib4(i-4)
    # prev_values[1] is fib4(i-3)
    # prev_values[2] is fib4(i-2)
    # prev_values[3] is fib4(i-1)
    prev_values = [f0, f1, f2, f3]

    current_val = 0

    for i in range(4, n + 1):
        # Sum the four previous elements
        sum_prev = (
            prev_values[0] + 
            prev_values[1] + 
            prev_values[2] + 
            prev_values[3]
        )

        current_val = sum_prev

        # Update the sliding window
        # Shift everything to the left:
        # The old index 1 becomes the new index 0
        # The old index 2 becomes the new index 1
        # The old index 3 becomes the new index 2
        # The new current_val becomes the new index 3
        prev_values[0] = prev_values[1]
        prev_values[1] = prev_values[2]
        prev_values[2] = prev_values[3]
        prev_values[3] = current_val

    return current_val