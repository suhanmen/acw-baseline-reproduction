def count_Squares(m, n):
    min_dim = min(m, n)
    total = 0
    for k in range(1, min_dim + 1):
        total += (m - k + 1) * (n - k + 1)
    return total