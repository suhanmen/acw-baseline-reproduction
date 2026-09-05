def search(arr, n):
    """
    Finds the element that appears only once in a sorted array.
    In a sorted array where all elements appear twice except for one,
    the single element can be found in O(log n) time using binary search.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        # If only one element is left
        if low == high:
            return arr[low]

        mid = (low + high) // 2

        # If mid is even, the pair should be at (mid, mid+1)
        # If mid is odd, the pair should be at (mid-1, mid)
        # We adjust mid to always represent the start of a potential pair
        if mid % 2 == 1:
            mid -= 1

        # If the pair is still intact, the single element is to the right
        if arr[mid] == arr[mid + 1]:
            low = mid + 2
        else:
            # If the pair is broken, the single element is to the left or is arr[mid]
            high = mid

    return -1