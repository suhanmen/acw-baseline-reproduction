def find_missing(sorted_array, n):
    """
    Find the missing number in a sorted array.
    The array is expected to be missing exactly one number up to 'n'.
    Uses binary search for efficiency.

    Args:
        sorted_array (list): Sorted list of integers with one missing number.
        n (int): The expected last number if no number were missing.

    Returns:
        int: The missing number.
    """
    if not sorted_array:
        return 1

    left, right = 0, len(sorted_array) - 1

    while left <= right:
        mid = (left + right) // 2
        expected = sorted_array[0] + mid
        if sorted_array[mid] == expected:
            left = mid + 1
        else:
            if mid == 0 or sorted_array[mid - 1] == expected - 1:
                return expected
            right = mid - 1

    if sorted_array[right] != n:
        return n

    return n