import math

def max_fill(grid, capacity):
    total = 0
    for row in grid:
        count = sum(row)
        if count == 0:
            continue
        total += math.ceil(count / capacity)
    return total