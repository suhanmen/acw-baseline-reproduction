def kth_element(arr, n, k):
    """
    Finds the kth smallest element in the first n elements of an array.
    The problem asserts imply k is 1-indexed (e.g., kth_element([12,3,5,7,19], 5, 2) == 3
    where 3 is the 2nd smallest among 5 elements).
    """
    # Slice the array to include first n elements
    subset = arr[:n]
    # Sort the subset to find the kth smallest
    subset.sort()
    # Return the kth element (k-1 because list is 0-indexed)
    return subset[k-1]