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

    # Step 1: Check if the list is empty or has fewer than 2 elements
    if len(lst) < 2:
        return None

    # Step 2: Sort the list to easily find the smallest elements
    sorted_lst = sorted(lst)

    # Step 3: Check if the first and second elements are the same
    if sorted_lst[0] == sorted_lst[1]:
        return None

    # Step 4: Return the second smallest element
    return sorted_lst[1]