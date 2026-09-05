def binomial_Coeff(n, k):
    if k < 0 or k > n or n < 0:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)  # Take advantage of symmetry to reduce computation
    numerator = 1
    for i in range(n - k + 1, n + 1):
        numerator *= i
    denominator = 1
    for i in range(1, k + 1):
        denominator *= i
    return numerator // denominator