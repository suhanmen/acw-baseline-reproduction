def set_left_most_unset_bit(n: int) -> int:
    if n == 0:
        return 1
    mask = n
    while mask & (mask + 1) == mask:
        mask = mask + 1
    return mask

assert set_left_most_unset_bit(10) == 14
assert set_left_most_unset_bit(12) == 14
assert set_left_most_unset_bit(15) == 15