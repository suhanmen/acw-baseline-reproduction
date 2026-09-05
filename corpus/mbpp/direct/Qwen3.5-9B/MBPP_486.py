from math import comb

def binomial_probability(n, k, p):
    """
    Computes the binomial probability P(X = k) for a binomial distribution
    with parameters n (number of trials) and p (probability of success).

    Formula: C(n, k) * p^k * (1 - p)^(n - k)
    """
    if k < 0 or k > n:
        return 0.0
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))