def frequency_lists(list_of_lists):
    """
    Finds the frequency count of all elements within a list of lists.

    Args:
        list_of_lists (list[list]): A list containing several sublists of integers.

    Returns:
        dict: A dictionary where keys are the unique elements from all sublists 
              and values are their respective counts.
    """
    frequency = {}
    for sublist in list_of_lists:
        for item in sublist:
            if item in frequency:
                frequency[item] += 1
            else:
                frequency[item] = 1
    return frequency