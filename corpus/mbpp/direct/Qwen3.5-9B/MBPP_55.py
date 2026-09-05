def tn_gp(n, a, r):
    """
    Calculate the nth term of a geometric series.

    Parameters:
    n (int): The position of the term to find (1-based index)
    a (int): The first term of the series
    r (int): The common ratio

    Returns:
    int: The nth term of the geometric series
    """
    if n < 1:
        raise ValueError("n must be a positive integer")
    return a * (r ** (n - 1))