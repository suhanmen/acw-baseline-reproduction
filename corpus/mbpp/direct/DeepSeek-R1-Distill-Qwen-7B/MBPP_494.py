def binary_to_integer(binary_tuple):
    binary_str = ''.join(str(bit) for bit in binary_tuple)
    return int(binary_str, 2)