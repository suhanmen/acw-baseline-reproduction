def cal_sum(n):
    if n < 0:
        return 0
    if n == 0:
        return 2
    if n == 1:
        return 2
    if n == 2:
        return 2

    perrin = [0, 2, 3]
    for _ in range(3, n + 1):
        perrin.append(perrin[_ - 2] + perrin[_ - 3])

    return sum(perrin[:n + 1])