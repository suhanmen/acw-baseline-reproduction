def is_octagonal(n):
    if n <= 0:
        return 0
    return n * (3 * n - 2)