def set_bit_number(n):
    msb = n.bit_length() - 1
    return 1 << msb