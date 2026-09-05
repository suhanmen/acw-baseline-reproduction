def remove_matching_tuple(tuples1, tuples2):
    set2 = set(tuples2)
    return [t for t in tuples1 if t not in set2]