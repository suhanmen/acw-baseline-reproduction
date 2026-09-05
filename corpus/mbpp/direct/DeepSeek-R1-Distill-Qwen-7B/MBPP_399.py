def bitwise_xor(tup1, tup2):
    return tuple(bin(x ^ y).count('1') for x, y in zip(tup1, tup2))