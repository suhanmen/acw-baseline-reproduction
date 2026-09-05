def extract_nth_element(data, n):
    """
    Extracts the nth element from a given list of tuples and returns them as a list.

    Args:
        data (list of tuples): A list where each element is a tuple.
        n (int): The index of the element to extract from each tuple.

    Returns:
        list: A list containing the nth elements from each tuple in the input list.
    """
    return [item[n] for item in data]