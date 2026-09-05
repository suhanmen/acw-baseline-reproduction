def is_num_decagonal(n):
    """
    Determines if a number is a decagonal number and returns the nth decagonal number.

    Args:
        n (int): The position in the decagonal sequence.

    Returns:
        int: The nth decagonal number if n is a valid positive integer.
        False: If the input is invalid or not a positive integer.
    """
    # Validate input
    if not isinstance(n, int) or n <= 0:
        return False

    # Calculate the nth decagonal number using the formula D_n = 4n² -3n
    decagonal = n * (4 * n - 3)

    return decagonal