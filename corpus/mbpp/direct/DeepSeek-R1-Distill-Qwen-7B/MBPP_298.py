def intersection_nested_lists(nested_list, given_list):
    # Flatten the nested list
    flat_list = [element for sublist in nested_list for element in sublist]

    # Convert given_list to a set for faster lookups
    given_set = set(given_list)

    # Collect elements present in both
    common_elements = [element for element in flat_list if element in given_set]

    # Reconstruct nested structure
    result = []
    current_index = 0
    for sublist in nested_list:
        if any(element in given_set for element in sublist):
            result.append(sublist)
        else:
            result.append([])

    return result