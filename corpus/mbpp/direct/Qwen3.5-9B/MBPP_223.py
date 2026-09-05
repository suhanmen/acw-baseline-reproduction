def is_majority(arr: list, n: int, candidate: int) -> bool:
    """
    Check if the given candidate is a majority element in a sorted array.
    A majority element appears more than n // 2 times.
    Since the array is sorted, we can use binary search to find the first and last occurrence.
    """
    if not arr or n == 0:
        return False

    # Helper to find the leftmost index of candidate
    def find_left():
        left, right = 0, n - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == candidate:
                result = mid
                right = mid - 1  # Look to the left
            elif arr[mid] < candidate:
                left = mid + 1
            else:
                right = mid - 1
        return result

    # Helper to find the rightmost index of candidate
    def find_right():
        left, right = 0, n - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == candidate:
                result = mid
                left = mid + 1  # Look to the right
            elif arr[mid] < candidate:
                left = mid + 1
            else:
                right = mid - 1
        return result

    first = find_left()
    if first == -1:
        return False  # Candidate not present

    last = find_right()
    count = last - first + 1

    return count > n // 2


# Quick verification against given assertions
if __name__ == "__main__":
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
    assert is_majority([1, 1, 1, 2, 2], 5, 1) == True
    print("All assertions passed.")