def next_Power_Of_2(n: int) -> int:
    if n < 1:
        return 1
    p = 1
    while p < n:
        p <<= 1
    return p