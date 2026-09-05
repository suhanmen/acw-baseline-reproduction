def add(lst):
    """Given a non-empty list of integers lst. Add the even elements that are at odd indices."""
    total = 0
    for index, num in enumerate(lst):
        if index % 2 == 1 and num % 2 == 0:
            total += num
    return total