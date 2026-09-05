def find_lucas(n):
    """
    Finds the n'th Lucas number.
    The Lucas sequence is defined as:
    L(0) = 2
    L(1) = 1
    L(n) = L(n-1) + L(n-2) for n > 1
    """
    if n == 0:
        return 2
    if n == 1:
        return 1

    a, b = 2, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b