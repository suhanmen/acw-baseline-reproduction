def find_lucas(n):
    """
    Find the n'th Lucas number.
    """
    # Check if the input is an integer
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")

    # Handle non-negative integers only
    if isinstance(n, int) and n < 0:
        raise ValueError("Input must be a non-negative integer.")

    # Base cases
    if n == 0:
        return 2
    elif n == 1:
        return 1

    # Initialize the first two Lucas numbers
    a, b = 2, 1  # L(0) and L(1)

    # Iteratively compute the Lucas numbers up to n
    for _ in range(2, n + 1):
        next_val = a + b
        b = a
        a = next_val

    return a