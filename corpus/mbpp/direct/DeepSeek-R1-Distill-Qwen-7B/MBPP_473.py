def tuple_intersection(tuples1, tuples2):
    intersection = set()
    for t1 in tuples1:
        for t2 in tuples2:
            if t1 == t2:
                intersection.add(t1)
    return frozenset(intersection)