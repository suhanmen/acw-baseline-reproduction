def closest_num(n):
    for i in range(n-1, 0, -1):
        if i == 1:
            return i
    return -1  # This line is theoretically unreachable since n starts from 1