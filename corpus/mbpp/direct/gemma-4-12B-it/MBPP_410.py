def min_val(lst):
    """
    Finds the minimum numeric value in a heterogeneous list.
    Filters out non-numeric types before calculating the minimum.
    """
    # Filter the list to keep only integers and floats
    numeric_values = [x for x in lst if isinstance(x, (int, float))]

    if not numeric_values:
        return None

    return min(numeric_values)