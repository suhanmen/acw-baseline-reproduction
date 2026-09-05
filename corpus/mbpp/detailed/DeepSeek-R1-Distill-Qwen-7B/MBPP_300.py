import math

def count_binary_seq(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")

    def binomial_coefficient(n, k):
        if k < 0 or k > n:
            return 0
        return math.comb(n, k)

    total = 0
    for k in range(n + 1):
        total += binomial_coefficient(n, k) ** 2

    return float(total)