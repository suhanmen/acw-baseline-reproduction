def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    # Convert both lists to sets to find unique elements and their intersection
    set1 = set(l1)
    set2 = set(l2)
    # Find the intersection of the two sets
    common_elements = set1 & set2
    # Convert the set to a sorted list
    return sorted(common_elements)