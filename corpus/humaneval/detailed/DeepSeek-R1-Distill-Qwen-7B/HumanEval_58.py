def common(l1: list, l2: list):
    """
    Return sorted unique common elements for two lists.
    """
    # Validate inputs
    if not isinstance(l1, list) or not isinstance(l2, list):
        raise TypeError("Both inputs must be lists.")

    # Handle cases where either list is empty
    if len(l1) == 0 or len(l2) == 0:
        return []

    # Convert lists to sets to find common elements
    set1 = set(l1)
    set2 = set(l2)

    # Find the intersection of the two sets
    common_elements = set1.intersection(set2)

    # Convert the set to a sorted list
    return sorted(common_elements)