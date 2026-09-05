def inversion_elements(tup):
    """
    Returns a tuple of differences where each element is:
    (element[i] - element[j]) for all i > j where tup[i] < tup[j].
    """
    result = []
    n = len(tup)
    for i in range(n):
        for j in range(i):
            if tup[i] < tup[j]:
                result.append(tup[j] - tup[i])
    return tuple(result)