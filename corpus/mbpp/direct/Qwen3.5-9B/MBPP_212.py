def fourth_Power_Sum(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += i ** 4
    return total