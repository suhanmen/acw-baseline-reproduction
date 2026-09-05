def cal_sum(n):
    # Initialize the first three perrin numbers
    perrin = [3, 0, 2]

    # Calculate perrin numbers up to n
    for i in range(3, n):
        next_num = perrin[i-1] + perrin[i-3]
        perrin.append(next_num)

    # Sum the perrin numbers up to n
    return sum(perrin[:n])