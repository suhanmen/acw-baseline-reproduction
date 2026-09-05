def average_Odd(n):
    if n < 1 or n % 2 == 0:
        raise ValueError("n must be an odd number greater than 0")
    count = 0
    total = 0
    for i in range(1, n+1, 2):
        count += 1
        total += i
    if count == 0:
        return 0  # to avoid division by zero, though the function should never reach here as n>=1
    return total // count