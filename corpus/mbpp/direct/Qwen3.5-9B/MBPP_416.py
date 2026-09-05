def breakSum(n):
    if n <= 1:
        return n
    if n == 2:
        return 1
    if n == 3:
        return 2

    max_sum = 0
    # Try all possible first splits
    for i in range(1, n):
        rest = n - i
        # Optimal for rest is either:
        # - break it further (if rest > 3, use the function result)
        # - don't break it further (rest itself, if rest <= 3)
        if rest <= 3:
            current_sum = i + rest
        else:
            current_sum = i + breakSum(rest)
        max_sum = max(max_sum, current_sum)

    return max_sum