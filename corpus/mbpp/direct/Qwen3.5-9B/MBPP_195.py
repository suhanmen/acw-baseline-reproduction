def first(arr, x, index):
    """
    Find the first occurrence of x in a sorted array using binary search.

    Parameters:
    arr (list): The sorted array
    x (int/float): The element to find
    index (int): The length of the array (provided for compatibility)

    Returns:
    int: The index of the first occurrence of x, or -1 if not found
    """
    left = 0
    right = index - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == x:
            result = mid
            right = mid - 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return result

# Verification
assert first([1,2,3,4,5,6,6],6,7) == 5
assert first([1,2,2,2,3,2,2,4,2],2,9) == 1
assert first([1,2,3],1,3) == 0