def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1."""
    if n > m:
        return -1
    # Calculate the sum of integers from n to m
    total = (m - n + 1) * (n + m) // 2
    # Calculate the average
    average = total / (m - n + 1)
    # Round the average to the nearest integer
    rounded = round(average)
    # Convert to binary and return as string prefixed with '0b'
    return f'0b{rounded}'