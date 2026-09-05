def highest_Power_of_2(n: int) -> int:
    if n < 1:
        raise ValueError("n must be at least 1")
    if n == 1:
        return 1
    p = 1
    while p * 2 <= n:
        p *= 2
    return p