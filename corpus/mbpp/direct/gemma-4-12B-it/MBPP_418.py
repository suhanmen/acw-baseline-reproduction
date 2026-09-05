def Find_Max(data):
    """
    Finds the sublist having the maximum length from a list of lists.
    If multiple sublists have the same maximum length, the first one encountered is returned.
    """
    if not data:
        return None

    max_sublist = data[0]
    max_length = len(data[0])

    for sublist in data:
        if len(sublist) > max_length:
            max_length = len(sublist)
            max_sublist = sublist

    return max_sublist