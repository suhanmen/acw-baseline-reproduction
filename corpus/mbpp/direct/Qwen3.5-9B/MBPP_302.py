def set_Bit_Number(n: int) -> int:
    """
    Find the most significant bit number which is also a set bit.
    Returns the 1-based position of the highest set bit.
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer.")

    msb = 1
    while n >= msb:
        msb <<= 1
    return msb >> 1