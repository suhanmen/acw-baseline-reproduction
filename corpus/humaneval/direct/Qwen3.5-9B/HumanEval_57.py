def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) <= 2:
        return True

    increasing = l[0] <= l[1]
    decreasing = l[0] >= l[1]

    if not increasing and not decreasing:
        return False

    for i in range(1, len(l) - 1):
        if increasing:
            if l[i] > l[i + 1]:
                return False
        else:  # decreasing
            if l[i] < l[i + 1]:
                return False

    return True