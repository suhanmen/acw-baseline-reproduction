def add_K_element(tuples_list, k):
    """
    Adds the value k to each element in every tuple within a list of tuples.

    Args:
        tuples_list (list of tuples): A list containing tuples of integers.
        k (int): The integer to add to each element.

    Returns:
        list of tuples: A list of tuples with k added to each element.
    """
    result = []
    for t in tuples_list:
        # Create a new tuple by adding k to every element in the original tuple
        new_tuple = tuple(element + k for element in t)
        result.append(new_tuple)
    return result