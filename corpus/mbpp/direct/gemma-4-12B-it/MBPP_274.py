import math

def even_binomial_Coeff_Sum(n):
    """
    Finds the sum of even index binomial coefficients (C(n, 0) + C(n, 2) + ...).
    The mathematical property states that the sum of even-indexed binomial
    coefficients for a power n is 2^(n-1) for n > 0.
    For n = 0, C(0, 0) = 1.
    """
    if n == 0:
        return 1
    return 2**(n - 1)

if __name__ == "__main__":
    assert even_binomial_Coeff_Sum(4) == 8
    assert even_binomial_Coeff_Sum(6) == 32
    assert even_binomial_Coeff_Sum(2) == 2