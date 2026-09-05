def is_woodall(n):
    if n <= 0:
        return False
    num_bits = n.bit_length()
    woodall_val = (1 << num_bits) - 1 + num_bits
    return n == woodall_val