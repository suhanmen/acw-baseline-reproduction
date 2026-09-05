def max_length_list(list_of_lists):
    """
    Finds the list with the maximum length from a list of lists.
    Returns a tuple containing the length of that list and the list itself.
    """
    if not list_of_lists:
        return (0, [])

    # Use max() with a lambda key to find the list with the greatest length
    longest_list = max(list_of_lists, key=lambda x: len(x))
    return (len(longest_list), longest_list)