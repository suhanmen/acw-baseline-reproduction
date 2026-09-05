def check_subset_list(main_list, subset_list):
    """
    Checks if subset_list is a subset of main_list.
    In this context, every element (which can be a list) in subset_list 
    must exist as an element in main_list.
    """
    # To handle nested lists correctly, we need to check if each element 
    # in subset_list is contained in main_list.
    # Since lists are not hashable, we can't easily use set operations 
    # if the elements are lists.

    # Convert main_list into a format that allows us to check for presence.
    # Since lists are not hashable, we compare the content.

    for item in subset_list:
        found = False
        for main_item in main_list:
            if main_item == item:
                found = True
                break
        if not found:
            return False
    return True

if __name__ == "__main__":
    assert check_subset_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]) == False
    assert check_subset_list([[2, 3, 1], [4, 5], [6, 8]], [[4, 5], [6, 8]]) == True
    assert check_subset_list([['a', 'b'], ['e'], ['c', 'd']], [['g']]) == False