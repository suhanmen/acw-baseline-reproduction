def centered_hexagonal_number(n):
    """
    Calculate the nth centered hexagonal number.

    The formula for the nth centered hexagonal number is:
    H_n = 3n(n-1) + 1

    Args:
        n (int): The position in the sequence (1-based index).

    Returns:
        int: The nth centered hexagonal number.
    """
    return 3 * n * (n - 1) + 1