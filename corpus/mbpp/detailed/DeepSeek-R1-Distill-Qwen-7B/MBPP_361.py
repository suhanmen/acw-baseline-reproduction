def remove_empty(lst):
    """
    Remove empty lists from a given list of lists.
    """
    result = []
    for element in lst:
        # Check if the element is a list and not empty
        if isinstance(element, list) and len(element) > 0:
            result.append(element)
    return result