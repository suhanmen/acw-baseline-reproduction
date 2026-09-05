def find_last_occurrence(arr, num):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == num:
            result = mid
            left = mid + 1  # Look for a later occurrence
        elif arr[mid] < num:
            left = mid + 1
        else:
            right = mid - 1

    return result