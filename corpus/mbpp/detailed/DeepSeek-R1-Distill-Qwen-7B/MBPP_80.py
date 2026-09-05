def tetrahedral_number(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")

    if n == 0:
        return 0.0

    tetrahedral = n * (n + 1) * (n + 2) / 6
    return tetrahedral