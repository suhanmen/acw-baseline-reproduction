def Find_Min_Length(sublists):
    """
    Finds the minimum length of a sublist within a list of lists.
    """
    if not sublists:
        return 0
    return min(len(sublist) for sublist in sublists)