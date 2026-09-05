def group_keyvalue(pairs):
    """
    Groups a sequence of key-value pairs into a dictionary of lists.

    Args:
        pairs (list of tuples): A list containing tuples of (key, value).

    Returns:
        dict: A dictionary where each key is mapped to a list of its values.
    """
    result = {}
    for key, value in pairs:
        if key not in result:
            result[key] = []
        result[key].append(value)
    return result