def sort_sublists(list_of_lists):
    """
    Sorts each sublist of strings in a given list of lists using a lambda function.
    """
    return [sorted(sublist, key=lambda x: x) for sublist in list_of_lists]