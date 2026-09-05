import math

def count_binary_seq(n: int) -> float:
    """
    Finds the count of binary sequences of length 2n such that the sum 
    of the first n bits is equal to the sum of the last n bits.

    The number of binary sequences of length n with sum k is given by 
    the binomial coefficient C(n, k).
    The problem asks for the sum of (C(n, k)^2) for k from 0 to n.
    Using the identity sum(C(n, k)^2) = C(2n, n).
    """
    # The identity sum(C(n, k) for k=0 to n)^2 = C(2n, n)
    # derives from Vandermonde's Identity.
    # Since the sums of the first n and last n bits must be equal,
    # if the sum is k (where 0 <= k <= n), there are C(n, k) ways 
    # to choose the first n bits and C(n, k) ways to choose the last n bits.
    # Total count = sum_{k=0}^n C(n, k) * C(n, k) = sum_{k=0}^n C(n, k)^2.

    return float(math.comb(2 * n, n))