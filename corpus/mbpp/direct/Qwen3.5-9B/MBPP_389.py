def find_lucas(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 2
    if n == 1:
        return 1
    a, b = 2, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b