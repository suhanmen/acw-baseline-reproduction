def Find_Min(sublists):
    """
    Finds the sublist with the minimum length.

    Args:
        sublists: A list of sublists.

    Returns:
        The sublist with the minimum length.
    """
    min_len = float('inf')
    min_list = []
    for s in sublists:
        if len(s) < min_len:
            min_len = len(s)
            min_list = s.copy()
    return min_list