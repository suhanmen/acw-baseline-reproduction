def is_majority(arr, n, x):
    """
    Checks if the element x is the majority element in a sorted array of size n.
    A majority element is an element that appears more than n / 2 times.
    """
    # Since the array is sorted, we can use binary search to find the first occurrence
    # and the last occurrence of x to determine its count efficiently.

    def find_first(arr, target):
        low, high = 0, n - 1
        first = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                first = mid
                high = mid - 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return first

    def find_last(arr, target):
        low, high = 0, n - 1
        last = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                last = mid
                low = mid + 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return last

    first_idx = find_first(arr, x)
    if first_idx == -1:
        return False

    last_idx = find_last(arr, x)
    count = last_idx - first_idx + 1

    return count > (n // 2)

if __name__ == "__main__":
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
    assert is_majority([1, 1, 1, 2, 2], 5, 1) == True