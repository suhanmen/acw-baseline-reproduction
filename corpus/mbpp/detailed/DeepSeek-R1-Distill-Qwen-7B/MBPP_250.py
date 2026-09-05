import inspect

def count_X(seq, target):
    """
    Count the occurrences of an element in a tuple.

    Args:
        seq: The tuple to search.
        target: The element to count.

    Returns:
        The number of times the target appears in the tuple.

    Raises:
        TypeError: If the first argument is not a tuple.
    """
    if not inspect.istuple(seq):
        raise TypeError("First argument must be a tuple.")

    count = 0
    for element in seq:
        if element == target:
            count += 1
    return count

# Test cases
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 4) == 0
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 10) == 3
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 8) == 4