def zigzag(n, k):
    """
    Returns the number at position (n, k) in a zigzag pattern where:
    - n is the row number (1-indexed)
    - k is the column number (1-indexed)
    The pattern fills diagonals starting from top-left (1,1) with sum = 2,
    alternating directions: down-right for even sums, up-right for odd sums.
    """
    # Sum of indices for the diagonal containing (n, k)
    diag = n + k

    # Number of elements in all previous diagonals (sums from 2 to diag-1)
    prev_count = (diag - 2) * (diag - 1) // 2

    # Determine direction: even diag sums go down-right (increasing n), odd sums go up-right (increasing k)
    if diag % 2 == 0:
        # Even diagonal: starts at (1, diag-1) and goes down-right to (diag-1, 1)
        # In this direction, column increases as we go down, but actually in even diagonals,
        # the pattern is: (1, diag-1), (2, diag-2), ..., (diag-1, 1)
        # So column = diag - row
        # We want to find how many steps down from top of this diagonal
        # Top of this diagonal is at row = 1, column = diag - 1
        steps = n - 1
        return prev_count + steps
    else:
        # Odd diagonal: starts at (diag-1, 1) and goes up-right to (1, diag-1)
        # Pattern: (diag-1, 1), (diag-2, 2), ..., (1, diag-1)
        # So row = diag - column
        # We want to find how many steps up from bottom of this diagonal
        # Bottom of this diagonal is at row = diag - 1, column = 1
        steps = diag - n
        return prev_count + steps

# Verification
assert zigzag(4, 3) == 5
assert zigzag(4, 2) == 4
assert zigzag(3, 1) == 1