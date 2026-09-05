def sum_gp(a, n, r):
    if r == 1:
        return a * n
    else:
        return a * (r**n - 1) // (r - 1)