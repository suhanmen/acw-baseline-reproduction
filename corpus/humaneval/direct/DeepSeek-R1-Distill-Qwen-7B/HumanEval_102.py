def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1."""
    if x > y:
        return -1
    # Find the smallest possible number >=x that is <=y and even
    start = x if x % 2 == 0 else x + 1
    if start > y:
        return -1
    # Iterate from start down to y to find the largest even
    for num in range(start, y - 1, -1):
        if num % 2 == 0:
            return num
    return -1