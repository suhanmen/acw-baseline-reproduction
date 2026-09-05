def hexagonal_num(n):
    """
    Calculate the nth hexagonal number.

    Args:
        n (int): The position in the hexagonal sequence.

    Returns:
        int: The nth hexagonal number.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    return n * (2 * n - 1)