def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.

    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
    # Use a set to get unique elements, then sort them
    unique_elements = sorted(list(set(lst)))

    # If there are fewer than 2 unique elements, the 2nd smallest doesn't exist
    if len(unique_elements) < 2:
        return None

    # Return the second element in the sorted list of unique values
    return unique_elements[1]