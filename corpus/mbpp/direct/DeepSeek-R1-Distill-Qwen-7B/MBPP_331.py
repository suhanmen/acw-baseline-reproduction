def count_unset_bits(num):
    total_bits = num.bit_length()
    set_bits = bin(num).count('1')
    return total_bits - set_bits