def sum_difference(n: int) -> int:
    squared_sum = sum(i ** 2 for i in range(1, n + 1))
    sum_squared = (n * (n + 1) // 2) ** 2
    return sum_squared - squared_sum