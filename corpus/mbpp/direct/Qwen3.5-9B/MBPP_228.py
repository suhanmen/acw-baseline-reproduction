def all_Bits_Set_In_The_Given_Range(n, l, r):
    """
    Check whether all bits in the range [l, r] are set in the given number n.

    Parameters:
    n (int): The number to check
    l (int): The left boundary of the range (inclusive)
    r (int): The right boundary of the range (inclusive)

    Returns:
    bool: True if all bits from position l to r are set in n, False otherwise
    """
    if l > r:
        return True

    # Create a mask with 1s from bit l to r
    if l == r:
        mask = 1 << l
    else:
        # Create mask with 1s from 0 to r: (1 << (r + 1)) - 1
        mask_full = (1 << (r + 1)) - 1
        # Remove 1s from 0 to l-1: mask_full - ((1 << l) - 1)
        mask = mask_full - ((1 << l) - 1)

    return (n & mask) == mask

# Verification tests
assert all_Bits_Set_In_The_Given_Range(4, 1, 2) == True
assert all_Bits_Set_In_The_Given_Range(17, 2, 4) == True
assert all_Bits_Set_In_The_Given_Range(39, 4, 6) == False