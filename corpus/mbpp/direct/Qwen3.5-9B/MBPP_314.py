def max_sum_rectangular_grid(grid, n):
    if n == 0:
        return 0
    if n == 1:
        return max(grid[0][0], grid[1][0])

    # dp[i][r] = maximum sum using columns 0..i, ending with column i and row r selected
    # But we cannot select both rows in same column if that violates "adjacent"?
    # Problem says: no two chosen numbers are adjacent. In a 2xn grid, adjacency includes:
    # - horizontally adjacent within same row (col j and j+1)
    # - vertically adjacent in same column (row 0 and row 1 at same col)
    # So in each column we can pick at most one cell, and we cannot pick consecutive columns.
    # This reduces to: choose a set of columns such that no two are consecutive,
    # and in each chosen column pick the larger of the two rows.

    if n == 1:
        return max(grid[0][0], grid[1][0])

    # Precompute best single cell per column
    best_col = [max(grid[0][i], grid[1][i]) for i in range(n)]

    # Now classic "house robber" on best_col
    dp = [0] * (n + 1)
    dp[1] = best_col[0]
    dp[2] = max(best_col[0], best_col[1])

    for i in range(3, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + best_col[i - 1])

    return dp[n]