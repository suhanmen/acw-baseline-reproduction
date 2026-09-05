def cal_sum(n):
    # Handle edge cases
    if n == 0:
        return 0
    elif n == 1:
        return 3
    elif n == 2:
        return 3  # 3 + 0
    else:
        # Initialize the Perrin sequence
        perrin = [3, 0, 2]
        for i in range(3, n):
            next_perrin = perrin[i-2] + perrin[i-3]
            perrin.append(next_perrin)
        # Calculate the sum
        return sum(perrin[:n])