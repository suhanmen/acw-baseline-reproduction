def same_order(a, b):
    # Check if either list is empty
    if not a or not b:
        return True

    # List to store common elements
    common = []

    # Collect common elements
    for item in a:
        if item in b:
            common.append(item)

    # Check the order of common elements
    for i, item in enumerate(common):
        # Get the index of item in both lists
        index_a = a.index(item)
        index_b = b.index(item)

        # If any common element is not in the same order, return False
        if index_b < index_a:
            return False

    # All common elements are in the same order
    return True