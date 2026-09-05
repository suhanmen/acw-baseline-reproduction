def extract_string(string_list, size):
    """
    Extracts strings from a given list that have a specific length.

    Args:
        string_list (list): A list of strings.
        size (int): The target length of the strings to extract.

    Returns:
        list: A list of strings that match the specified length.
    """
    return [s for s in string_list if len(s) == size]