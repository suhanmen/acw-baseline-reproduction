def even_bit_toggle_number(n):
    mask = 0x55  # Binary: 0101 0101 0101 0101
    return n ^ mask