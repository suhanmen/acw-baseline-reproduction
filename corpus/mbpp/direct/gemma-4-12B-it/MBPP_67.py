def bell_number(n: int) -> int:
    """
    Calculates the n-th Bell number, which represents the number of 
    ways to partition a set of n elements into non-empty subsets.
    """
    if n == 0:
        return 1

    # We use the Bell Triangle (also known as Aitken's array or Peirce triangle)
    # to compute the Bell numbers efficiently.
    # The first row is [1]
    # Each subsequent row starts with the last number of the previous row.
    # Each subsequent number in a row is the sum of the number to its left 
    # and the number above it in the previous row.

    bell_triangle = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    bell_triangle[0][0] = 1

    for i in range(1, n + 1):
        # First element of current row is the last element of the previous row
        bell_triangle[i][0] = bell_triangle[i-1][i-1]

        # Fill the rest of the row
        for j in range(1, i + 1):
            bell_triangle[i][j] = bell_triangle[i][j-1] + bell_triangle[i-1][j-1]

    # The n-th Bell number is the first element of the n-th row 
    # (or the last element of the (n-1)-th row, depending on indexing).
    # With our construction, it is the first element of the n-th row.
    return bell_triangle[n][0]