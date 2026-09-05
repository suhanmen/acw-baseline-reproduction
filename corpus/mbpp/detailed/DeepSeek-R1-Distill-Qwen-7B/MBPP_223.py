import bisect

def is_majority(arr, element, count):
    """
    Check if the given element is a majority element in the given sorted array.
    A majority element appears more than half the time in the array.
    """
    if not arr or arr[-1] != element:
        return False

    n = len(arr)
    required = n // 2 + 1  # More than half

    left = bisect.bisect_left(arr, element)
    right = bisect.bisect_right(arr, element)

    count_occurrences = right - left
    return count_occurrences >= count

# Test cases
assert is_majority([1, 2, 3, 3, 3, 3, 10], 3, 4) == True
assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 4, 5) == False
assert is_majority([1, 1, 1, 2, 2], 1, 3) == True