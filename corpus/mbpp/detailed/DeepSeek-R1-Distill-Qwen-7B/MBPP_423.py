def get_maxgold(grid, start_row, steps):
    # Input validation
    if not grid or not grid[0] or steps <= 0:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    if steps >= rows * cols:
        return sum(grid[start_row])

    # Initialize DP table
    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    # Fill the first step
    for col in range(cols):
        dp[start_row][col] = grid[start_row][col]

    # Fill the remaining steps
    for step in range(1, steps):
        for row in range(rows):
            for col in range(cols):
                if row == 0 and col == 0:
                    # Only cell (0,0) can be reached from itself
                    dp[row][col] = max(dp[row][col], dp[row][col] + grid[row][col])
                else:
                    max_val = 0
                    # Possible moves: up, up-left, up-right, left, right, down, down-left, down-right
                    # Check all possible previous cells that can move to current cell
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if dr == 0 and dc == 0:
                                continue  # Skip current cell
                            prev_row = row - dr
                            prev_col = col - dc
                            if prev_row >= 0 and prev_row < rows and prev_col >= 0 and prev_col < cols:
                                if dp[prev_row][prev_col] + grid[row][col] > max_val:
                                    max_val = dp[prev_row][prev_col] + grid[row][col]
                    dp[row][col] = max(dp[row][col], max_val)

    # The result is the maximum value in the last step's DP table
    return max(dp[start_row][start_col] for start_col in range(cols))