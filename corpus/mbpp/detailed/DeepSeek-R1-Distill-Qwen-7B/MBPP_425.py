def count_element_in_list(lst, element):
    """
    Count the number of sublists containing a particular element.

    Args:
        lst: A list of lists (sublists) where each sublist can contain any elements.
        element: The element to count in each sublist.

    Returns:
        The count of sublists that contain the specified element.

    Raises:
        TypeError: If the input is not a list of lists or if the element is not hashable.
    """
    # First, validate the inputs
    if not isinstance(lst, list):
        raise TypeError("The first argument must be a list.")

    for sublist in lst:
        if not isinstance(sublist, list):
            raise TypeError("All elements of the first argument must be lists.")

    if not isinstance(element, hashable):
        raise TypeError("The element to search for must be hashable.")

    # Initialize the count and the intermediate list to store sublist information
    count = 0
    found_elements = []  # This will store tuples of (is_element_present, sublist)

    # Iterate through each sublist
    for sublist in lst:
        # Check if the current sublist contains the element
        contains_element = False
        for item in sublist:
            if item == element:
                contains_element = True
                break

        # If the element is present, record the information
        if contains_element:
            found_elements.append(True)
        else:
            found_elements.append(False)

    # Count how many sublists contain the element
    count = sum(found_elements)

    return count