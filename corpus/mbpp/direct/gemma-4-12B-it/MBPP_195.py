def first(arr, n, target):
    """
    Finds the first position of an element in a sorted array.
    Note: The problem description says 'sorted array', but the provided 
    test cases include [1,2,2,2,3,2,2,4,2], which is not strictly sorted.
    To satisfy the assertions provided, we must find the first occurrence 
    of 'target' in the array 'arr'.
    """
    try:
        return arr.index(target)
    except ValueError:
        return -1