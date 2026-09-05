def unique(l: list):
    """
    Return sorted unique elements in a list

    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    if not isinstance(l, list):
        raise ValueError("Input must be a list")

    # Convert to a set to remove duplicates, then back to list
    unique_elements = list(set(l))

    # Sort the list
    unique_elements.sort()

    return unique_elements