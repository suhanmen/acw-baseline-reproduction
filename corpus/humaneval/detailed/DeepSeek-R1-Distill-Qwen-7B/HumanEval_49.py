def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).

    Handles various edge cases:
    - p=1 returns 0
    - negative n returns 0
    - computes efficiently using pow with three arguments

    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    if p == 1:
        return 0
    if n < 0:
        return 0
    return pow(2, n, p)