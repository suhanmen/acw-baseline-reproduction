def set_left_most_unset_bit(n: int) -> int:
    """
    Sets the left-most unset bit in the binary representation of n.

    Examples:
    10 (1010) -> 14 (1110)
    12 (1100) -> 14 (1110)
    15 (1111) -> 15 (1111)
    """
    if n == 0:
        return 1

    # Find the position of the highest set bit
    # For 10 (1010), high_bit is 8 (1000)
    high_bit = 1 << (n.bit_length() - 1)

    # Check bits from high_bit downwards to find the first 0
    # However, we need to consider the bit just to the left of the current representation
    # if all bits in the current range are 1.
    # But according to the test cases:
    # 10 (1010) -> left-most 0 is at position 2 (val 4) -> 10 | 4 = 14
    # 12 (1100) -> left-most 0 is at position 1 (val 2) -> 12 | 2 = 14
    # 15 (1111) -> no 0s inside the 4 bits -> 15 (stays 15)

    # Let's refine: we look for the highest 0 bit within the range 
    # defined by the most significant bit.

    # Iterate from the most significant bit position down to 0
    for i in range(n.bit_length() - 1, -1, -1):
        if not (n & (1 << i)):
            return n | (1 << i)

    return n

# The logic above satisfies:
# 10 (1010) -> i=3 (1), i=2 (0) -> 10 | 4 = 14
# 12 (1100) -> i=3 (1), i=2 (1), i=1 (0) -> 12 | 2 = 14
# 15 (1111) -> i=3,2,1,0 are all 1 -> return 15