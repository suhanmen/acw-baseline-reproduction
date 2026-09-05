def overlapping(list1, list2):
    """
    Checks whether there is any common element (overlap) 
    between two sequences.
    """
    # Convert to sets to find the intersection
    set1 = set(list1)
    set2 = set(list2)

    # Check if the intersection is non-empty
    return not set1.isdisjoint(set2)

if __name__ == "__main__":
    assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
    assert overlapping([1,2,3],[4,5,6]) == False
    assert overlapping([1,4,5],[1,4,5]) == True