def breakSum(n):
    if n < 2:
        return n
    max_sum = 0
    for i in range(1, n):
        for j in range(i, n - i + 1):
            k = n - i - j
            current_sum = breakSum(i) + breakSum(j) + breakSum(k)
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum