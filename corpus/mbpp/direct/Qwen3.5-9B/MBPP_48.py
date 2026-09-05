def odd_bit_set_number(n: int) -> int:
    """Set all odd-positioned bits (1st, 3rd, 5th, ...) of the given number to 1."""
    mask = 0
    bit = 1
    for i in range(32):
        if i % 2 == 0:  # positions 0, 2, 4... correspond to 1st, 3rd, 5th bits if counting from 1
            mask |= bit
        bit <<= 1
    return n | mask