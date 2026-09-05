def remove_matching_tuple(list_one: list[tuple], list_two: list[tuple]) -> list[tuple]:
    """
    Removes any tuple from list_one that is present in list_two.

    Args:
    list_one: The first list of tuples from which elements are to be removed.
    list_two: The second list of tuples used as the reference for matching.

    Returns:
    A new list containing tuples from list_one that do not have a matching tuple in list_two.

    Raises:
    TypeError: If either argument is not a list or if any element within the lists is not a tuple.
    """
    # Validate list_one type
    if not isinstance(list_one, list):
        raise TypeError("The first argument must be a list.")

    # Validate list_two type
    if not isinstance(list_two, list):
        raise TypeError("The second argument must be a list.")

    # Initialize a list to hold the results
    result_list = []

    # Iterate through each element in list_one
    for candidate_tuple in list_one:
        # Validate that the element in list_one is a tuple
        if not isinstance(candidate_tuple, tuple):
            raise TypeError(f"An element in the first list is not a tuple: {candidate_tuple!r}")

        is_match_found = False

        # Iterate through each element in list_two to find a match
        for reference_tuple in list_two:
            # Validate that the element in list_two is a tuple
            if not isinstance(reference_tuple, tuple):
                raise TypeError(f"An element in the second list is not a tuple: {reference_tuple!r}")

            # Check if the current tuple from list_one matches the current tuple from list_two
            # Using tuple equality (==) which checks content
            if candidate_tuple == reference_tuple:
                is_match_found = True
                break

        # If no match was found in list_two, append to the result list
        if not is_match_found:
            result_list.append(candidate_tuple)

    return result_list