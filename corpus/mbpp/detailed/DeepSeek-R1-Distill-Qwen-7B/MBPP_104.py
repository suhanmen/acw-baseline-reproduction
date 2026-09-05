def sort_sublists(lst):
    """
    Sorts each sublist of strings in a given list of lists lexicographically.

    Args:
        lst (list of list of str): The input list of lists containing strings.

    Returns:
        list of list of str: A new list of lists where each sublist is sorted.
    """
    # Sort each sublist
    sorted_sublists = [sorted(sublist) for sublist in lst]
    return sorted_sublists