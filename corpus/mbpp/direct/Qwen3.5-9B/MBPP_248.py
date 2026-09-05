def harmonic_sum(n):
    if n <= 1:
        return 1.0
    result = 1.0
    for i in range(2, n):
        result += 1.0 / i
    return result