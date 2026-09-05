def count_Squares(m, n):
    """
    Counts the total number of squares of all sizes in an m x n rectangle.
    The formula is the sum of min(i, j) for all sizes k from 1 to min(m, n).
    Specifically, there are (m - k + 1) * (n - k + 1) squares of size k x k.
    """
    count = 0
    # The largest possible square size is the minimum of the two dimensions
    for k in range(1, min(m, n) + 1):
        count += (m - k + 1) * (n - k + 1)
    return count