def convert_list_dictionary(list1, list2, list3):
    """
    Converts multiple lists into a list of nested dictionaries.

    Args:
        list1 (list): List of keys for the outer dictionary.
        list2 (list): List of keys for the inner dictionary.
        list3 (list): List of values for the inner dictionary.

    Returns:
        list: A list of nested dictionaries.
    """
    result = []
    for i in range(len(list1)):
        # Create a nested dictionary for each index
        nested_dict = {list1[i]: {list2[i]: list3[i]}}
        result.append(nested_dict)
    return result