def count_first_elements(data):
    """
    Finds the count of elements that occur before the first nested tuple 
    in a given tuple.
    """
    count = 0
    for item in data:
        if isinstance(item, tuple):
            break
        count += 1
    return count