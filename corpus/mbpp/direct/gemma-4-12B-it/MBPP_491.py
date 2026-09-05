def sum_gp(a, r, n):
    """
    Finds the sum of a geometric progression series.

    Args:
    a (int/float): The first term.
    r (int/float): The common ratio.
    n (int): The number of terms.

    Returns:
    int/float: The sum of the series.
    """
    if r == 1:
        return a * n
    else:
        return a * (1 - r**n) / (1 - r)

if __name__ == "__main__":
    assert sum_gp(1, 5, 2) == 31
    assert sum_gp(1, 5, 4) == 341
    assert sum_gp(2, 6, 3) == 728