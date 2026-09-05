def tuple_intersection(list1, list2):
    """
    Finds the intersection of two lists of tuples, where order within the tuples 
    doesn't matter. Returns a set of sorted tuples.
    """
    def normalize(t):
        return tuple(sorted(t))

    # Normalize all tuples in both lists to a standard sorted form
    set1 = {normalize(t) for t in list1}
    set2 = {normalize(t) for t in list2}

    # Find intersection of the normalized sets
    return set1.intersection(set2)