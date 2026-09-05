def remove_matching_tuple(tuple_list1, tuple_list2):
    """
    Removes the matching tuples from the first list of tuples 
    if they appear exactly in the second list of tuples.
    """
    # Use a set for O(1) average lookup time
    to_remove = set(tuple_list2)

    # Construct a new list excluding tuples present in the removal set
    result = [t for t in tuple_list1 if t not in to_remove]

    return result