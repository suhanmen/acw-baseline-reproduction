def highest_Power_of_2(n):
    return 1 << (n.bit_length() - 1)