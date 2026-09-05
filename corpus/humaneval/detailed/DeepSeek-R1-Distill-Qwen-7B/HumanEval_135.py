def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Check if the array is empty
    if not arr:
        return -1

    # If there's only one element, return index 0
    if len(arr) == 1:
        return 0

    # Initialize the result with -1
    result = -1

    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # Check if current element is less than the previous one
        if arr[i] < arr[i - 1]:
            result = i

    return result