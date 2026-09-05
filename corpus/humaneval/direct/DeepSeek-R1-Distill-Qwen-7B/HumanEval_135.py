def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values."""
    largest_index = -1
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            largest_index = i
    return largest_index