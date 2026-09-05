def sum_series(n):
    result = 0
    while n > 0:
        result += n
        n -= 2
    return result