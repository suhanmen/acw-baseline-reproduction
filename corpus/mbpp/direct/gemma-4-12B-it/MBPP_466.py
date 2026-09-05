def find_peak(arr, n):
    """
    Finds a peak element in an array.
    A peak element is an element that is strictly greater than its neighbors.
    For the boundaries, we consider them having neighbors of -infinity.
    This implementation uses a binary search approach to find a peak in O(log n) time.
    """
    if n == 0:
        return -1
    if n == 1:
        return 0

    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        # Check if mid is a peak
        left_val = arr[mid - 1] if mid > 0 else float('-inf')
        right_val = arr[mid + 1] if mid < n - 1 else float('-inf')

        if arr[mid] >= left_val and arr[mid] >= right_val:
            return mid

        # If the element to the right is greater, the peak must be on the right side
        if mid < n - 1 and arr[mid + 1] > arr[mid]:
            low = mid + 1
        else:
            # Otherwise, the peak must be on the left side
            high = mid - 1

    return -1