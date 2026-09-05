def maximum(a, b):
    """
    Finds the maximum of two numbers a and b.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The maximum of a and b.

    Raises:
        ValueError: If either a or b is not an integer.
    """
    # Helper function to determine the maximum of two numbers without using the max function.
    def _max(x, y):
        if x > y:
            return x
        elif y > x:
            return y
        else:
            return x  # or y, since they are equal

    # Validate inputs
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Both arguments must be integers.")

    # Handle the case where both numbers are equal
    if a == b:
        return a

    # Find the maximum using the helper function
    return _max(a, b)