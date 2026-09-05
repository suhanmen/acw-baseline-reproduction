def tetrahedral_number(n):
    """
    Calculate the nth tetrahedral number.
    The nth tetrahedral number is the sum of the first n triangular numbers.
    Formula: T(n) = n * (n + 1) * (n + 2) / 6
    """
    if n < 1:
        raise ValueError("n must be a positive integer")
    return float(n * (n + 1) * (n + 2) // 6)