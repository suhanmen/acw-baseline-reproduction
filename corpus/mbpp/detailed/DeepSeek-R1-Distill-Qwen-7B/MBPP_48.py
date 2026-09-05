def odd_bit_set_number(n):
    # Create a mask with bits set at all odd positions
    # For 64-bit numbers, the mask is 0xAAAAAAAAAAAAAAAA
    mask = 0xAAAAAAAAAAAAAAAA
    # Apply the mask using bitwise OR
    result = n | mask
    return result