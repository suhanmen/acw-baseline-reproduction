def count_Squares(m, n):
    # Ensure m is the smaller dimension
    m, n = sorted((m, n))
    total = 0
    # For each possible square size from 1x1 up to mxm
    for size in range(1, m+1):
        # Number of positions horizontally
        horizontal = n - size + 1
        # Number of positions vertically
        vertical = m - size + 1
        # Total squares of this size
        total += horizontal * vertical
    return total

# Test cases to verify the solution
assert count_Squares(4,3) == 20
assert count_Squares(2,2) == 5
assert count_Squares(1,1) == 1