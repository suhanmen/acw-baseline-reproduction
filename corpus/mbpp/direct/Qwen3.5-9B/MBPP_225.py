def find_min(arr, low, high):
    if low > high:
        return None
    if low == high:
        return arr[low]

    mid = (low + high) // 2

    if mid < high and arr[mid] > arr[mid + 1]:
        return arr[mid + 1]
    if mid > low and arr[mid] < arr[mid - 1]:
        return arr[mid]

    if arr[low] < arr[mid]:
        return find_min(arr, low, mid - 1)
    return find_min(arr, mid + 1, high)