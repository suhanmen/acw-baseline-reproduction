from typing import List

def get_maxgold(gold_mine: List[List[int]], rows: int, cols: int) -> int:
    """
    Solves the Gold Mine problem using dynamic programming.

    The goal is to find the maximum gold that can be collected starting from 
    the bottom row and moving upwards. From a cell (r, c), you can move 
    to (r-1, c-1), (r-1, c), or (r-1, c+1) in the row above, provided 
    those cells are within the grid boundaries.

    Args:
        gold_mine: A 2D list of integers representing gold at each cell.
        rows: Number of rows in the grid.
        cols: Number of columns in the grid.

    Returns:
        The maximum amount of gold reachable.
    """
    # --- Input Validation ---
    if not isinstance(gold_mine, list) or not gold_mine:
        raise ValueError("Input gold_mine must be a non-empty list of lists.")

    if rows <= 0 or cols <= 0:
        return 0

    # Ensure the dimensions provided match the actual data
    actual_rows = len(gold_mine)
    if actual_rows != rows:
        raise ValueError(f"Expected {rows} rows, but found {actual_rows}.")

    for i in range(rows):
        if len(gold_mine[i]) != cols:
            raise ValueError(f"Row {i} has length {len(gold_mine[i])}, but expected {cols}.")

    # Handle the edge case of an empty grid or single element
    if rows == 0 or cols == 0:
        return 0
    if rows == 1:
        # If only one row exists, the max gold is the max value in that row
        return max(gold_mine[0]) if gold_mine[0] else 0

    # --- Dynamic Programming Setup ---
    # We create a DP table of the same dimensions as the gold_mine.
    # dp[r][c] will store the maximum gold reachable starting from 
    # the bottom up to cell (r, c).

    # Use a copy of the grid to store accumulated results to avoid
    # mutating the input list.
    dp = [row[:] for row in gold_mine]

    # --- Core Logic ---
    # We start from the second row from the bottom (index 1) and move up.
    # The bottom row (index rows-1) is already initialized with its own gold values.
    for r in range(rows - 2, -1, -1):
        for c in range(cols):
            # Identify the potential paths from the current cell (r, c) 
            # to the row above (r+1).
            # Wait, the standard Gold Mine logic usually defines movement as:
            # "From cell (r, c), you can move to (r-1, c-1), (r-1, c), or (r-1, c+1)"
            # Or equivalently, from cell (r, c), you look at the results of the row below.

            # Because the problem structure implies moving towards the top, 
            # we calculate the value of a cell based on the three possible cells 
            # in the row immediately below it.

            # Option 1: Directly below
            path_down = dp[r + 1][c]

            # Option 2: Bottom-left
            path_down_left = 0
            if c - 1 >= 0:
                path_down_left = dp[r + 1][c - 1]

            # Option 3: Bottom-right
            path_down_right = 0
            if c + 1 < cols:
                path_down_right = dp[r + 1][c + 1]

            # The maximum gold from the row below
            max_from_below = max(path_down, path_down_left, path_down_right)

            # Current cell's max value is its own gold + max from possible paths below
            dp[r][c] = gold_mine[r][c] + max_from_below

    # The answer is the maximum value in the top row of our DP table.
    # In this specific problem formulation (bottom-up accumulation),
    # the maximum value is found in the first row's results.

    # However, since we are calculating "max gold from (r,c) to the bottom",
    # the result is the maximum value in the first row (index 0).
    # Let's verify the logic: 
    # If we start at (r, c) and move to (r-1, c-1/c/c+1), 
    # it's the same as starting at the bottom and moving up to the top.

    result = max(dp[0])
    return result

# The logic above uses the "bottom-up" approach: 
# dp[r][c] = gold[r][c] + max(dp[r+1][c-1], dp[r+1][c], dp[r+1][c+1])
# This correctly identifies the max path from any cell in the top row to the bottom.