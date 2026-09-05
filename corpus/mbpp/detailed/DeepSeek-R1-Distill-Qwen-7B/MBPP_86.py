def centered_hexagonal_number(n):
    """
    Calculate the nth centered hexagonal number.

    Args:
        n (int): The position in the centered hexagonal sequence.

    Returns:
        int: The nth centered hexagonal number.

    Raises:
        ValueError: If n is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")

    # Calculate the nth centered hexagonal number
    try:
        result = 3 * n * (n - 1) + 1
    except OverflowError:
        raise ValueError("n is too large for the calculation to fit in an integer")

    return result