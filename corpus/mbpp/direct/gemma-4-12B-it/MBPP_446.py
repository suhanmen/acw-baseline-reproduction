def count_Occurrence(tup, lst):
    """
    Counts the occurrences of all elements of a list within a tuple.
    """
    count = 0
    # Convert list to set to ensure we only count each requested element's 
    # total occurrences in the tuple exactly once if that's the intended logic,
    # however, based on the assertions provided:
    # ('a', 'a', 'c', 'b', 'd'), ['a', 'b'] -> 'a' appears twice, 'b' appears once. 2+1 = 3.
    # (1, 2, 3, 1, 4, 6, 7, 1, 4), [1, 4, 7] -> 1 appears 3 times, 4 appears 2 times, 7 appears 1 time. 3+2+1 = 6.
    # (1,2,3,4,5,6), [1,2] -> 1 appears once, 2 appears once. 1+1 = 2.

    for item in lst:
        count += tup.count(item)
    return count