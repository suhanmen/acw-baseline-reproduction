def count_element_in_list(list_of_lists, element):
    """
    Counts the number of sublists within a nested list that contain a specific element.

    Args:
        list_of_lists (list): A list containing sublists.
        element: The item to search for within the sublists.

    Returns:
        int: The count of sublists containing the element.
    """
    count = 0
    for sublist in list_of_lists:
        if element in sublist:
            count += 1
    return count