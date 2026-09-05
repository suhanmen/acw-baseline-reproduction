def max_sum_rectangular_grid(grid, n):
    """
    Finds the maximum sum such that no two chosen numbers are adjacent 
    in a 2 x n grid.

    Adjacency is defined as horizontal or vertical.
    Two numbers are adjacent if they share an edge.
    """
    if n == 0:
        return 0
    if n == 1:
        return max(grid[0][0], grid[1][0])

    # dp[i][state] represents the maximum sum using the first i columns
    # where state is a bitmask representing the rows chosen in column i.
    # State 0: None chosen in column i
    # State 1: Only row 0 chosen in column i
    # State 2: Only row 1 chosen in column i
    # State 3: Both row 0 and row 1 chosen in column i (Invalid because they are adjacent)

    # Since we cannot pick two adjacent numbers, state 3 is impossible.
    # Valid states per column are:
    # 0: None (00)
    # 1: Row 0 (01)
    # 2: Row 1 (10)

    # dp[i][j] is the max sum up to column i, with column i in state j.
    dp = [[0] * 3 for _ in range(n)]

    # Base case for the first column
    dp[0][0] = 0
    dp[0][1] = grid[0][0]
    dp[0][2] = grid[1][0]

    for i in range(1, n):
        # Current state 0 (None chosen in column i)
        # Can follow any valid state in column i-1
        dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])

        # Current state 1 (Row 0 chosen in column i)
        # Cannot have Row 0 chosen in column i-1 (horizontal adjacency)
        # Can follow State 0 or State 2 in column i-1
        dp[i][1] = grid[0][i] + max(dp[i-1][0], dp[i-1][2])

        # Current state 2 (Row 1 chosen in column i)
        # Cannot have Row 1 chosen in column i-1 (horizontal adjacency)
        # Can follow State 0 or State 1 in column i-1
        dp[i][2] = grid[1][i] + max(dp[i-1][0], dp[i-1][1])

    return max(dp[n-1])