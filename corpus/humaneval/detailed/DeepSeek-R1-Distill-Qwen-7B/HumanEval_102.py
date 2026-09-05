def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # Input validation
    if not isinstance(x, int) or not isinstance(y, int):
        return -1
    if x < 1 or y < 1:
        return -1
    if x > y:
        return -1

    # Iterate from y downwards to x
    current = y
    while current >= x:
        if current % 2 == 0:
            return current
        current -= 1
    return -1