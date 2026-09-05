def common_element(list1, list2):
    """
    Returns True if there is at least one common element between list1 and list2.
    Returns None otherwise.
    """
    set1 = set(list1)
    set2 = set(list2)

    # Find the intersection of the two sets
    intersection = set1.intersection(set2)

    if intersection:
        return True
    else:
        return None

if __name__ == "__main__":
    assert common_element([1,2,3,4,5], [5,6,7,8,9]) == True
    assert common_element([1,2,3,4,5], [6,7,8,9]) == None
    assert common_element(['a','b','c'], ['d','b','e']) == True