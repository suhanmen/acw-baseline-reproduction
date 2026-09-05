def remove_tuples(tuples_list, k):
    """
    Removes all tuples from the list that have a length equal to k.
    """
    return [t for t in tuples_list if len(t) != k]