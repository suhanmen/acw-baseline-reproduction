def list_split(lst, n):
    """
    Splits a list into n sublists where each sublist contains elements
    at every nth position starting from different offsets.

    Example:
    list_split(['a', 'b', 'c', 'd', 'e', 'f'], 2) 
    -> [['a', 'c', 'e'], ['b', 'd', 'f']]
    """
    result = []
    for i in range(n):
        result.append(lst[i::n])
    return result