def specified_element(two_d_list, specified_element):
    """
    Extracts every specified element from each sublist of a 2D list.

    Args:
        two_d_list: A list of lists where each sublist has the same length.
        specified_element: An integer indicating which element to extract from each sublist.

    Returns:
        A list containing the specified elements from each sublist.

    Raises:
        ValueError: If specified_element is out of bounds or not an integer.
    """
    # Check if the specified_element is an integer
    if not isinstance(specified_element, int):
        raise ValueError("specified_element must be an integer")

    # Check if specified_element is within the valid range
    sublist_length = len(two_d_list[0]) if two_d_list else 0
    if specified_element < 0 or specified_element >= sublist_length:
        raise ValueError("specified_element is out of bounds")

    # Handle empty input
    if not two_d_list:
        return []

    result = []
    for sublist in two_d_list:
        result.append(sublist[specified_element])

    return result