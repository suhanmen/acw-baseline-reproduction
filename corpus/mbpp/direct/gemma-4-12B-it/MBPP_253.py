def count_integer(lst):
    """
    Counts the number of integers in a given list.

    Args:
        lst (list): A list containing various types of elements.

    Returns:
        int: The count of elements that are of type 'int' and not 'bool'.
    """
    count = 0
    for item in lst:
        # Use type(item) is int to exclude booleans, as bool is a subclass of int.
        if type(item) is int:
            count += 1
    return count