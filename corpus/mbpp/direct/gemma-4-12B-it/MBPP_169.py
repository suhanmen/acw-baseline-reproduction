def get_pell(n: int) -> int:
    """
    Calculates the nth Pell number.
    The Pell sequence is defined as:
    P(0) = 0
    P(1) = 1
    P(n) = 2*P(n-1) + P(n-2) for n > 1
    """
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, 2 * b + a
    return b

if __name__ == "__main__":
    assert get_pell(4) == 12
    assert get_pell(7) == 169
    assert get_pell(8) == 408