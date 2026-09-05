def smallest_missing(arr, left, right):
    left_bound = left
    right_bound = right
    while left_bound <= right_bound:
        mid = (left_bound + right_bound) // 2
        if mid > len(arr) - 1 or (mid < len(arr) and arr[mid] == mid):
            right_bound = mid - 1
        else:
            left_bound = mid + 1
    return left_bound