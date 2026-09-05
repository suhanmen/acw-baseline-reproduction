def rotate_left(lst, n):
    """
    Rotate a given list to the left by specified number of items.
    """
    if not lst:
        return []
    n = n % len(lst)
    return lst[n:] + lst[:n]