def smallest_missing(arr, start, end):
    """
    Finds the smallest missing non-negative integer in a sorted array.
    Uses binary search to achieve O(log n) complexity.
    """
    # Special case: If the first element is not 0, the smallest missing is 0.
    if arr[start] != 0:
        return 0

    low = start
    high = end

    while low <= high:
        mid = (low + high) // 2

        # The expected value at index 'mid' if no elements are missing 
        # (given that arr[0] is 0) is simply 'mid'.
        if arr[mid] == mid:
            # Everything to the left is correct, look to the right.
            low = mid + 1
        else:
            # There is a gap somewhere to the left (including mid).
            high = mid - 1

    # After the loop, 'low' will be the index of the first mismatch,
    # which corresponds to the value of the smallest missing element.
    return low