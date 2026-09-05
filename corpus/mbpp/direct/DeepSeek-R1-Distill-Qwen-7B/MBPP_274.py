def even_binomial_Coeff_Sum(n):
    from math import comb
    return sum(comb(n, k) for k in range(0, n+1, 2))