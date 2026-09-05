def find_rotation_count(arr):
    if not arr:
        return 0
    if arr[0] <= arr[-1]:
        return 0
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    return left