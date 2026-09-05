def encode_list(data):
    """
    Encodes a list or a string into a run-length encoding format.
    The output is a list of lists, where each sub-list contains 
    [count, value].
    """
    if not data:
        return []

    result = []
    # Handle string input by converting it to a list of characters
    if isinstance(data, str):
        iterable = list(data)
    else:
        iterable = data

    if not iterable:
        return []

    current_val = iterable[0]
    current_count = 0

    for item in iterable:
        if item == current_val:
            current_count += 1
        else:
            result.append([current_count, current_val])
            current_val = item
            current_count = 1

    result.append([current_count, current_val])
    return result