def sum_Of_Series(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += i ** 3
    return total