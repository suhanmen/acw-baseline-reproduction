import math

def count_binary_seq(n: int) -> float:
    # The count is sum_{k=0}^{n} (C(n, k) * C(n, k))
    # which equals C(2n, n)
    return math.comb(2 * n, n)