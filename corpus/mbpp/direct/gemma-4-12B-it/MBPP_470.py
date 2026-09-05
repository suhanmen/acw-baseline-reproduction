def add_pairwise(tup: tuple) -> tuple:
    """
    Returns a tuple of the pairwise addition of the elements of the given tuple.
    Example: (1, 5, 7, 8, 10) -> (1+5, 5+7, 7+8, 8+10) -> (6, 12, 15, 18)
    """
    result = []
    for i in range(len(tup) - 1):
        result.append(tup[i] + tup[i+1])
    return tuple(result)