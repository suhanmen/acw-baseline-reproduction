def max_sum_rectangular_grid(grid, n):
    if n == 0:
        return 0
    # dp[i][0]: max sum up to i-th column without taking grid[0][i]
    # dp[i][1]: max sum up to i-th column with taking grid[0][i]
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = grid[0][0]
    dp[0][1] = max(grid[0][0], grid[0][1])
    for i in range(1, n):
        dp[1][i] = max(dp[0][i-1], dp[1][i-1]) + grid[1][i]
        dp[0][i] = max(dp[0][i-1], dp[1][i-1]) + grid[0][i]
    return max(dp[0][n-1], dp[1][n-1])

# Test cases
assert max_sum_rectangular_grid([[1, 4, 5], [2, 0, 0]], 3) == 7
assert max_sum_rectangular_grid([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], 5) == 24
assert max_sum_rectangular_grid([[7, 9, 11, 15, 19], [21, 25, 28, 31, 32]], 5) == 81