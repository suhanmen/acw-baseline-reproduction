def next_perfect_square(n):
    root = int(n ** 0.5)
    if root * root == n:
        return (root + 1) ** 2
    else:
        return (root + 1) ** 2