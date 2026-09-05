def next_Power_of_2(n):
    if n == 0:
        return 1
    n -= 1
    highest_bit = n.bit_length()
    return 1 << highest_bit