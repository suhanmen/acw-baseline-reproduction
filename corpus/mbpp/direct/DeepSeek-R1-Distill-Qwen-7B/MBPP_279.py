def is_num_decagonal(n):
    return 3 * n ** 2 - 2 * n

assert is_num_decagonal(3) == 27
assert is_num_decagonal(7) == 175
assert is_num_decagonal(10) == 370