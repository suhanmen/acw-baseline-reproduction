def even_bit_toggle_number(n: int) -> int:
    return n ^ 0xAAAAAAAA

assert even_bit_toggle_number(10) == 15
assert even_bit_toggle_number(20) == 1
assert even_bit_toggle_number(30) == 11