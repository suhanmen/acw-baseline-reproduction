def count_Squares(m: int, n: int) -> int:
    """
    Counts the number of squares of all sizes that can be formed
    within a rectangle of dimensions m x n.
    """
    total_squares = 0
    # The largest possible square side is the minimum of the two dimensions
    max_side = min(m, n)

    # A square of side length 'k' can be placed in (m - k + 1) * (n - k + 1) positions
    for k in range(1, max_side + 1):
        total_squares += (m - k + 1) * (n - k + 1)

    return total_squares