def get_maxgold(gold, rows, cols):
    """
    Solves the gold mine problem using dynamic programming.
    The goal is to find the maximum gold reachable starting from any 
    point in the first row and moving only down, down-left, or down-right.
    """
    if not gold or rows == 0:
        return 0

    # Create a DP table to store the maximum gold collected reaching each cell
    # We can modify the input grid in-place or use a copy to preserve the original
    dp = [row[:] for row in gold]

    # Iterate through each row starting from the second row (index 1)
    for r in range(1, rows):
        for c in range(cols):
            # Possible values from the row above:
            # Directly above
            res = dp[r-1][c]

            # Above-left
            if c > 0:
                res = max(res, dp[r-1][c-1])

            # Above-right
            if c < cols - 1:
                res = max(res, dp[r-1][c+1])

            # Update the current cell with the max gold collected so far
            dp[r][c] += res

    # The answer is the maximum value found in the last row
    return max(dp[rows-1])

# Test cases
if __name__ == "__main__":
    assert get_maxgold([[1, 3, 1, 5],[2, 2, 4, 1],[5, 0, 2, 3],[0, 6, 1, 2]], 4, 4) == 16
    assert get_maxgold([[10, 20], [30, 40]], 2, 2) == 70
    assert get_maxgold([[4, 9], [3, 7]], 2, 2) == 13