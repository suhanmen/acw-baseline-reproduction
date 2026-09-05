def sequential_search(arr, target):
    """
    Perform a sequential search to find the target element in the given array.
    Returns a tuple (found, index) where found is a boolean indicating if the element was found,
    and index is the position of the element if found, otherwise -1.
    """
    if not arr:
        return (False, -1)

    index = 0
    found = False

    for element in arr:
        if element == target:
            found = True
            break
        index += 1

    if found:
        return (True, index)
    else:
        return (False, -1)