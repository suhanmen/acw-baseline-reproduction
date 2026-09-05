def sum_gp(a, l, n):
    """
    Calculate the sum of a geometric progression series.

    Parameters:
    a (int): First term
    l (int): Common ratio
    n (int): Number of terms

    Returns:
    int: Sum of the geometric progression
    """
    if n <= 0:
        return 0
    if l == 1:
        return a * n
    return a * (l ** n - 1) // (l - 1)