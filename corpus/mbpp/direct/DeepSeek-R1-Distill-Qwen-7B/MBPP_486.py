import math

def binomial_probability(n, k, p):
    q = 1.0 - p
    comb = math.comb(n, k)
    prob = comb * (p ** k) * (q ** (n - k))
    return prob