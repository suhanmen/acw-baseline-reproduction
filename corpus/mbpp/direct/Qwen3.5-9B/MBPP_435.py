def last_Digit(n: int) -> int:
    return n % 10 if n >= 0 else (-n) % 10

assert last_Digit(123) == 3
assert last_Digit(25) == 5
assert last_Digit(30) == 0