def set_left_most_unset_bit(n):
    """
    Set the leftmost unset bit of a given integer.

    Args:
        n (int): The input integer. Non-positive integers are returned as is.

    Returns:
        int: The modified integer with the leftmost unset bit set to 1.
    """
    if n <= 0:
        return n

    # Calculate the next power of two greater than n
    power = 1
    while power <= n:
        power <<= 1

    # Add 1 to the power to set all bits to the right to 1
    return power + 1