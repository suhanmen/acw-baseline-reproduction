from typing import Optional, List, Tuple

def _validate_input(n: int) -> None:
    """
    Validates that the input integer n is within the acceptable range for this function.

    The problem defines fib4(n) for non-negative integers.
    Negative integers are considered invalid input for this sequence definition.

    Parameters:
    n (int): The input integer to validate.

    Raises:
    ValueError: If n is negative.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    if n < 0:
        raise ValueError("Input n must be a non-negative integer. Received: {}".format(n))

def _get_base_case_value(n: int) -> int:
    """
    Determines the value of the Fib4 sequence based on the defined base cases.

    Base cases:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0

    Parameters:
    n (int): The index to determine the base case for.

    Returns:
    int: The corresponding value from the base cases.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        # This should not be reached due to external validation,
        # but included for internal logic completeness if called independently.
        raise ValueError("Unexpected base case index: {}".format(n))

def _compute_fib4_iterative(n: int) -> int:
    """
    Computes the n-th Fib4 number using an iterative approach with explicit state management.

    This function implements the recurrence relation:
    fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

    It maintains the last four computed values in a list to avoid recursion
    and to achieve O(n) time complexity with O(1) space complexity (excluding the fixed-size buffer).

    Parameters:
    n (int): The index of the Fib4 sequence to compute.

    Returns:
    int: The n-th number in the Fib4 sequence.
    """

    # Initialize a list to hold the history of computed values.
    # We start with the known base cases.
    # History will store [fib4(0), fib4(1), fib4(2), fib4(3)] initially.
    history: List[int] = [0, 0, 2, 0]

    # If the requested index is within the pre-computed base cases, return immediately.
    if n < len(history):
        return history[n]

    # Current index we are trying to compute.
    current_index: int = len(history)

    # Loop until we reach the target index.
    while current_index < n:
        # Retrieve the last four values from our history.
        # Since we need n-1, n-2, n-3, n-4, and our list is 0-indexed:
        # fib4(current_index-1) is at history[-1]
        # fib4(current_index-2) is at history[-2]
        # etc.
        prev_1: int = history[-1]
        prev_2: int = history[-2]
        prev_3: int = history[-3]
        prev_4: int = history[-4]

        # Apply the recurrence relation.
        next_value: int = prev_1 + prev_2 + prev_3 + prev_4

        # Append the newly computed value to our history.
        history.append(next_value)

        # Move the current index forward.
        current_index += 1

    # The final value in the history list is the result for index n.
    return history[-1]

def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.

    Parameters:
    n (int): A non-negative integer representing the index in the Fib4 sequence.

    Returns:
    int: The n-th element of the Fib4 sequence.

    Raises:
    TypeError: If n is not an integer.
    ValueError: If n is negative.

    Examples:
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """

    # Step 1: Explicitly validate the input.
    _validate_input(n)

    # Step 2: Compute the result using the iterative helper.
    result: int = _compute_fib4_iterative(n)

    # Step 3: Return the computed result.
    return result