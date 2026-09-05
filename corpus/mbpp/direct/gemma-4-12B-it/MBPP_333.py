def Sort(lst):
    """
    Sorts a list of sublists based on the second element of each sublist.
    """
    return sorted(lst, key=lambda x: x[1])