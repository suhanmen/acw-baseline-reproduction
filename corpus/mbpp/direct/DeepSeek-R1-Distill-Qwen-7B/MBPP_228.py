def all_Bits_Set_In_The_Given_Range(number, lower_bound, upper_bound):
    """
    Check whether all the bits are set in the given range.

    Args:
        number (int): The number to check.
        lower_bound (int): The lower bound of the range.
        upper_bound (int): The upper bound of the range.

    Returns:
        bool: True if all bits in the given range are set, False otherwise.
    """
    for i in range(lower_bound, upper_bound + 1):
        mask = 1 << i
        if (number & mask) == 0:
            return False
    return True