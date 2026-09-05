def find_lists(tuple_data):
    """
    Counts the number of list objects present within the given tuple.
    """
    count = 0
    for item in tuple_data:
        if isinstance(item, list):
            count += 1
    return count