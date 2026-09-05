def max_val(lst):
    """
    Finds the maximum numerical value in a heterogeneous list.
    Filters out non-numeric types (strings, None, etc.) and 
    returns the maximum of the remaining numbers.
    """
    numbers = [x for x in lst if isinstance(x, (int, float))]
    if not numbers:
        return None
    return max(numbers)