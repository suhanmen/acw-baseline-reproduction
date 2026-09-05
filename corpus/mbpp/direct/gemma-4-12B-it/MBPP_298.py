def intersection_nested_lists(main_list, nested_lists):
    """
    Finds elements within nested lists that are also present in a main list.
    Returns a list of lists, where each sub-list contains elements from the
    corresponding sub-list in nested_lists that exist in main_list.
    """
    # Use a set for O(1) average lookup time
    main_set = set(main_list)
    result = []

    for sub_list in nested_lists:
        # Preserve the order of elements as they appear in the nested list
        intersection = [item for item in sub_list if item in main_set]
        result.append(intersection)

    return result