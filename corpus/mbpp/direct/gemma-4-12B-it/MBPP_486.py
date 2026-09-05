import math

def binomial_probability(n, k, p):
    """
    Computes the binomial probability of exactly k successes in n independent 
    Bernoulli trials with success probability p.

    Formula: P(X = k) = (n choose k) * (p^k) * ((1-p)^(n-k))
    """
    # Calculate combinations (n choose k)
    combinations = math.comb(n, k)

    # Calculate the probability
    probability = combinations * (p ** k) * ((1 - p) ** (n - k))

    return probability