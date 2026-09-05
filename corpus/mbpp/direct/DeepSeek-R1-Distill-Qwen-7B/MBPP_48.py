def odd_bit_set_number(n):
    # The mask has 1s in all odd bit positions.
    mask = 0xAAAAAAAA  # In binary: 101010... which covers all odd bits up to 32 bits.
    # To set all odd bits, we OR the number with the mask.
    return n | mask