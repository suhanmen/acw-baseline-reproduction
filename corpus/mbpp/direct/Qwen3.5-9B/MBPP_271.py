def even_Power_Sum(n):
    total = 0
    for i in range(1, n + 1):
        even_num = 2 * i
        total += even_num ** 5
    return total