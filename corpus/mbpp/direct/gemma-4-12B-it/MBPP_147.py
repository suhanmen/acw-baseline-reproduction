def max_path_sum(triangle, rows, cols):
    """
    Finds the maximum total path sum in a given triangle.
    The path starts from the top and moves to adjacent numbers in the next row.

    Args:
        triangle: A 2D list representing the triangle.
        rows: The number of rows (not used in the core calculation but provided in signature).
        cols: The number of columns (not used in the core calculation but provided in signature).

    Returns:
        The maximum sum.
    """
    # We use dynamic programming to solve this from bottom to top.
    # We create a copy of the last row to store the maximum paths.
    # However, it's cleaner to work on a copy or a result table.

    # Create a 2D array representing the triangle values to avoid mutating input
    dp = [row[:] for row in triangle]

    # Start from the second to last row and move upwards
    for r in range(rows - 2, -1, -1):
        for c in range(len(dp[r])):
            # The max path sum at this cell is the cell's value 
            # plus the maximum of the two possible children below it.
            dp[r][c] += max(dp[r+1][c], dp[r+1][c+1])

    return dp[0][0]

if __name__ == "__main__":
    # The assertions provided in the prompt
    assert max_path_sum([[1, 0, 0], [4, 8, 0], [1, 5, 3]], 2, 2) == 14
    assert max_path_sum([[13, 0, 0], [7, 4, 0], [2, 4, 6]], 2, 2) == 24 
    assert max_path_sum([[2, 0, 0], [11, 18, 0], [21, 25, 33]], 2, 2) == 53