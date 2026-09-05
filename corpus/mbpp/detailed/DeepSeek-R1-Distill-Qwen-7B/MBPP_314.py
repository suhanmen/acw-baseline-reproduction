def max_sum_rectangular_grid(grid, n):
    if n == 0:
        return 0
    # Initialize DP table
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = grid[0][0]
    dp[1][0] = grid[1][0]

    for i in range(1, n):
        # Take from first row, cannot take from first row of previous column
        dp[0][i] = grid[0][i] + max(dp[1][i-1], dp[0][i-1])
        # Take from second row, cannot take from second row of previous column
        dp[1][i] = grid[1][i] + max(dp[0][i-1], dp[1][i-1])

    return max(dp[0][n-1], dp[1][n-1])

# Test the function
assert max_sum_rectangular_grid([[1, 4, 5], [2, 0, 0]], 3) == 7
assert max_sum_rectangular_grid([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], 5) == 24
assert max_sum_rectangular_grid([[7, 9, 11, 15, 19], [21, 25, 28, 31, 32]], 5) == 81