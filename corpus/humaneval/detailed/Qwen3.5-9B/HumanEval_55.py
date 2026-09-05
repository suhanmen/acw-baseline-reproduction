def _is_valid_fibonacci_index(value: int) -> bool:
    """
    Validate that the input is a non-negative integer suitable for Fibonacci indexing.

    Parameters:
    value (int): The number to validate

    Returns:
    bool: True if the value is valid, False otherwise
    """
    if not isinstance(value, int):
        return False
    if isinstance(value, bool):
        return False
    if value < 0:
        return False
    return True


def _compute_fibonacci_iterative(n: int) -> int:
    """
    Compute the n-th Fibonacci number using an iterative approach with explicit steps.

    This function uses memoization via temporary variables to track the previous two
    Fibonacci numbers in the sequence.

    Parameters:
    n (int): The index of the Fibonacci number to compute (0-based)

    Returns:
    int: The n-th Fibonacci number

    Algorithm:
    - F(0) = 0
    - F(1) = 1
    - F(n) = F(n-1) + F(n-2) for n > 1

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Initialize the first two Fibonacci numbers
    prev2 = 0  # Represents F(i-2)
    prev1 = 1  # Represents F(i-1)
    current = 0  # Will represent F(i)

    # Iterate from 2 up to n to compute the sequence
    for i in range(2, n + 1):
        # Calculate the current Fibonacci number as sum of previous two
        current = prev1 + prev2

        # Update prev2 to be the previous prev1
        prev2 = prev1

        # Update prev1 to be the current value calculated
        prev1 = current

    # After the loop completes, current holds F(n)
    return current


def _handle_edge_cases_and_validation(n: int) -> int:
    """
    Validate input and handle all edge cases explicitly before computation.

    Parameters:
    n (int): The input number

    Returns:
    int: The computed Fibonacci number

    Raises:
    TypeError: If n is not an integer or is a boolean
    ValueError: If n is negative
    """
    # Explicit type checking to exclude booleans (since bool is subclass of int in Python)
    if isinstance(n, bool):
        raise TypeError(f"Parameter n must be an integer, not a boolean. Received type: {type(n)}")

    # Check if n is actually an integer
    if not isinstance(n, int):
        raise TypeError(f"Parameter n must be an integer. Received type: {type(n).__name__}")

    # Validate non-negative constraint
    if n < 0:
        raise ValueError(f"Parameter n must be non-negative. Received value: {n}")

    # Handle the base cases explicitly before entering general logic
    if n == 0:
        return 0
    if n == 1:
        return 1

    # If we reach here, n is a valid integer >= 2
    # Defer the actual computation to the dedicated iterative function
    return _compute_fibonacci_iterative(n)


def fib(n: int):
    """Return n-th Fibonacci number.

    The Fibonacci sequence is defined as:
    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2) for n > 1

    Parameters:
    n (int): The index of the Fibonacci number to retrieve (must be >= 0)

    Returns:
    int: The n-th Fibonacci number

    Raises:
    TypeError: If n is not an integer (excluding bools)
    ValueError: If n is negative

    Examples:
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    >>> fib(0)
    0
    >>> fib(-1)
    Traceback (most recent call last):
        ...
    ValueError: Parameter n must be non-negative. Received value: -1
    """
    # Perform validation and compute the result
    result = _handle_edge_cases_and_validation(n)

    return result