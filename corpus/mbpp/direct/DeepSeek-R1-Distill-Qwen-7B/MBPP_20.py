def is_woodall(n):
    if n <= 1:
        return False
    return (n - 1) & (n - 2) == 0