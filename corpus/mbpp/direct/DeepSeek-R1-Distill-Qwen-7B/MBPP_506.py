def permutation_coefficient(n, k):
    if k < 0 or k > n:
        return 0
    result = 1
    for i in range(k):
        result *= (n - i)
    return result