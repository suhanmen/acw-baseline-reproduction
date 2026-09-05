def sum_series(n):
    total = 0
    current = n
    while current > 0:
        total += current
        current -= 2
    return total