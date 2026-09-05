def No_of_Triangle(n, m):
    if m < 1 or m > (n - 1):
        return -1
    return (n - 1) * n * (2 * n - 1) // 6