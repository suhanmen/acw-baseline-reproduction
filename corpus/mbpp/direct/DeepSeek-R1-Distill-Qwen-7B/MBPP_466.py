def find_peak(arr, n):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if mid == 0 or mid == n - 1:
            if arr[mid] >= arr[mid + 1]:
                return mid
            else:
                return mid - 1
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid
        elif arr[mid] < arr[mid - 1]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

assert find_peak([1, 3, 20, 4, 1, 0], 6) == 2
assert find_peak([2, 3, 4, 5, 6], 5) == 4
assert find_peak([8, 9, 11, 12, 14, 15], 6) == 5