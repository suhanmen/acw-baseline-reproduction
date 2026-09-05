def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """

    # Validate inputs
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Both arguments must be integers")

    # Handle edge cases explicitly
    # Edge case: both numbers are zero
    if x == 0 and y == 0:
        return 0

    # Edge case: one number is zero
    if x == 0 or y == 0:
        return x + y

    # Degenerate case: negative numbers
    if x < 0 or y < 0:
        # Handle case with only one negative number
        if x < 0 and y >= 0:
            result = y - abs(x)
            return result if result >=0 else 0
        elif y < 0 and x >=0:
            result = x - abs(y)
            return result if result >=0 else 0
        # Both numbers are negative
        result = x + y
        return result if result >=0 else 0

    # General case: both numbers are positive
    return x + y