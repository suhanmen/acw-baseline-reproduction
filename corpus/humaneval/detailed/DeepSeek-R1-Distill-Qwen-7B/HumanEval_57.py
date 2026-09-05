def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.

    An empty list or a list with a single element is considered monotonic.
    A list where all elements are equal is also considered monotonic.

    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    # Handle edge cases: empty list or single element
    if len(l) <= 1:
        return True

    # Check for non-decreasing order
    is_increasing = True
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            is_increasing = False
            break

    # Check for non-increasing order
    is_decreasing = True
    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            is_decreasing = False
            break

    # If either condition is met, return True; else, False
    return is_increasing or is_decreasing