def max_length(list_of_lists):
    """
    Finds the list within a list of lists that has the maximum length.
    Returns a tuple containing the length of that list and the list itself.
    """
    if not list_of_lists:
        return (0, [])

    # Use the built-in max function with key=len to find the longest sublist
    longest_list = max(list_of_lists, key=len)
    return (len(longest_list), longest_list)