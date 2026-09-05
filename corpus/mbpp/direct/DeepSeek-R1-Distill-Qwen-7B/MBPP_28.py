def binomial_Coeff(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)  # Take advantage of symmetry
    numerator = 1
    for i in range(n, n - k, -1):
        numerator *= i
    denominator = 1
    for i in range(1, k + 1):
        denominator *= i
    return numerator // denominator