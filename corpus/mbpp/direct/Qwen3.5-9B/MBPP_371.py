def smallest_missing(arr, low, high):
    """
    Find the smallest missing element in a sorted array using binary search.

    :param arr: A sorted list of integers.
    :param low: The lower bound index (inclusive).
    :param high: The upper bound index (exclusive).
    :return: The smallest missing non-negative integer.
    """
    if high - low == 0:
        return 0

    if arr[low] != 0:
        return 0

    left, right = low, high - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if the element at mid is equal to its index
        # arr[i] == i implies 0, 1, 2... are present up to i
        if arr[mid] == mid:
            # All elements from 0 to arr[mid] are present
            # Missing element must be in the right half
            left = mid + 1
        else:
            # arr[mid] > mid, meaning some number is missing in the left half
            right = mid - 1

    # left points to the first index where arr[index] != index
    # The missing number is exactly 'left'
    return left

# Verification examples
# assert smallest_missing([0, 1, 2, 3, 4, 5, 6], 0, 6) == 7
# assert smallest_missing([0, 1, 2, 6, 9, 11, 15], 0, 6) == 3
# assert smallest_missing([1, 2, 3, 4, 6, 9, 11, 15], 0, 7) == 0