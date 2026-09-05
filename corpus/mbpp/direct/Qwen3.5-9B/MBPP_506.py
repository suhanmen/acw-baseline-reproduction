def permutation_coefficient(n, k):
    if k > n or k < 0:
        return 0
    result = 1
    for i in range(k):
        result *= (n - i)
    return result