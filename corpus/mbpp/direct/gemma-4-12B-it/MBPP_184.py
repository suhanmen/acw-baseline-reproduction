def greater_specificnum(lst, num):
    """
    Returns True if all elements in the list are greater than the specified number,
    otherwise returns False.
    """
    if not lst:
        return False
    return all(x > num for x in lst)