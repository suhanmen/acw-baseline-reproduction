def is_Sum_Of_Powers_Of_Two(n):
    return (n & (n - 1)) == 0 and n != 0