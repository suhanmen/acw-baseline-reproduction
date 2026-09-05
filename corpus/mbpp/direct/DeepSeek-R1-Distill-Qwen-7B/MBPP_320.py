def sum_difference(n):
    sum_n = n * (n + 1) // 2
    sum_sq_n = n * (n + 1) * (2 * n + 1) // 6
    return sum_n ** 2 - sum_sq_n