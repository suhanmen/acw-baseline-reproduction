def is_Sum_Of_Powers_Of_Two(n):
    if n <= 0:
        return False
    while n % 2 == 0:
        n = n // 2
    return n == 1