def find_tuples(tuple_list, k):
    """
    Finds tuples where every element is divisible by k.
    Returns the result as a string representation of a list.
    """
    result = []
    for tup in tuple_list:
        if all(x % k == 0 for x in tup):
            result.append(tup)
    return str(result)