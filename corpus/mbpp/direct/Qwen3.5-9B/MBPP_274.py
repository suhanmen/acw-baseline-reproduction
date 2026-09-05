def even_binomial_Coeff_Sum(n: int) -> int:
    """
    Returns the sum of binomial coefficients at even indices: C(n,0) + C(n,2) + C(n,4) + ...
    This sum is equal to 2^(n-1) for n > 0, and 1 for n = 0.
    """
    if n == 0:
        return 1
    return 1 << (n - 1)