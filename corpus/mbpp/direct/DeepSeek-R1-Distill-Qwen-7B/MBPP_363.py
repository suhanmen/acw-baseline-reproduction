def add_K_element(tuples, k):
    """
    Adds k elements to each element in the tuple.
    """
    return [(x + k for x in t) for t in tuples]