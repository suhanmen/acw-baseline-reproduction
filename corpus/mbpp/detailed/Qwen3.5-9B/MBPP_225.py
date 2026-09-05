def validate_index(index: int) -> None:
    """
    Validates that the given index is a non-negative integer.

    Raises:
        TypeError: If the index is not an integer.
        ValueError: If the index is negative.
    """
    if not isinstance(index, int):
        raise TypeError(f"Index must be an integer, got {type(index).__name__}")
    if index < 0:
        raise ValueError(f"Index must be non-negative, got {index}")


def validate_array(array) -> None:
    """
    Validates that the input is a list of integers.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    if not isinstance(array, list):
        raise TypeError(f"Input must be a list, got {type(array).__name__}")
    if len(array) == 0:
        raise ValueError("Input list cannot be empty")

    for i, item in enumerate(array):
        if not isinstance(item, int):
            raise TypeError(f"All elements must be integers, found {type(item).__name__} at index {i}")


def is_sorted_increasing(sub_array: list, start_idx: int, end_idx: int) -> bool:
    """
    Checks if the sub-array from start_idx to end_idx (inclusive) is sorted in increasing order.

    Args:
        sub_array: The full array to check within.
        start_idx: Starting index of the sub-array.
        end_idx: Ending index of the sub-array.

    Returns:
        True if sorted in increasing order, False otherwise.
    """
    for i in range(start_idx, end_idx):
        if sub_array[i] > sub_array[i + 1]:
            return False
    return True


def find_min_linear(array: list, start: int, end: int) -> int:
    """
    Finds the minimum element in a sorted array using a linear scan.
    This is used when the array is fully sorted (no rotation) or as a fallback.

    Args:
        array: The list of integers.
        start: Starting index of the search range.
        end: Ending index of the search range.

    Returns:
        The minimum element found.
    """
    min_value = array[start]

    for i in range(start + 1, end + 1):
        if array[i] < min_value:
            min_value = array[i]

    return min_value


def find_min_rotated_binary_search(array: list, start: int, end: int) -> int:
    """
    Finds the minimum element in a sorted and rotated array using binary search.

    Logic:
    1. Compare the middle element with the end element.
    2. If array[mid] > array[end], the minimum must be in the right half.
    3. Otherwise, the minimum is in the left half (including mid).

    This relies on the property that a rotated sorted array consists of two sorted subarrays.

    Args:
        array: The list of integers (sorted and rotated).
        start: Starting index of the current search range.
        end: Ending index of the current search range.

    Returns:
        The minimum element in the rotated array.
    """
    while start <= end:
        # If start and end are adjacent, pick the smaller one
        if start == end:
            return array[start]

        if start + 1 == end:
            return array[start] if array[start] < array[end] else array[end]

        mid = (start + end) // 2

        # Ensure mid does not equal start to avoid infinite loops in edge cases,
        # though the loop condition handles termination.
        if mid == start:
            # This case happens when end == start + 1 and mid rounds to start
            # handled by start+1 == end check above, but added for safety logic clarity
            return array[start] if array[start] < array[end] else array[end]

        # Check if the left part [start...mid] is sorted
        if array[start] < array[mid]:
            # The minimum is either array[start] or in the right part [mid+1...end]
            # Since left is sorted, the first element of the sorted segment (if rotated)
            # would be the start of the next cycle, but here we know array[start] is a local min candidate.
            # Actually, if left part is sorted, the minimum must be on the right side of mid
            # UNLESS the rotation point is at the very beginning (array[start] is min).
            # However, in a rotated array:
            # If array[start] < array[mid], the minimum is either array[start] (if no rotation in this segment)
            # or it is to the right of mid.
            # But wait, if the array is [4, 5, 1, 2, 3], start=0, end=4, mid=2.
            # array[0]=4, array[2]=1. 4 < 1 is False. So we go right. Correct.
            # If array is [1, 2, 3, 4, 5], start=0, end=4, mid=2.
            # array[0]=1, array[2]=3. 1 < 3 is True. Min is in left (0..2).
            # We take the left half [start...mid].

            # Special check: if the left part is strictly increasing and covers the whole range?
            # If array[start] <= array[end], the whole segment is sorted.
            if array[start] <= array[end]:
                return array[start]

            # Otherwise, the minimum is in the right half (mid + 1 to end)
            start = mid + 1

        else:
            # array[start] > array[mid] implies the pivot (minimum) is in [start...mid]
            # because the sequence decreases from start to mid at some point.
            end = mid

    # Fallback (should theoretically not be reached if logic is correct)
    return array[start]


def find_min(array: list, start: int, end: int) -> int:
    """
    Finds the minimum element in a sorted and rotated array.

    The function performs input validation first.
    It determines if the array segment is fully sorted.
    If fully sorted, it returns the first element (which is the minimum).
    Otherwise, it uses binary search to find the minimum in O(log n) time.

    Args:
        array: The list of integers, which is assumed to be sorted and rotated.
        start: The starting index of the search range (inclusive).
        end: The ending index of the search range (inclusive).

    Returns:
        The minimum integer value in the specified range of the array.

    Raises:
        TypeError: If inputs are not of expected types (list, int).
        ValueError: If the input list is empty or indices are out of bounds.
    """
    # Step 1: Validate the input array structure and contents
    validate_array(array)

    # Step 2: Validate the indices
    validate_index(start)
    validate_index(end)

    n = len(array)

    # Step 3: Check if indices are within valid bounds
    if start < 0 or end >= n or start > end:
        raise ValueError(f"Indices {start} and {end} are out of bounds for array of length {n}")

    # Step 4: Check for degenerate cases where start and end are the same
    if start == end:
        return array[start]

    # Step 5: Check if the entire range [start, end] is sorted in non-decreasing order.
    # If it is sorted, the minimum is simply the first element.
    if is_sorted_increasing(array, start, end):
        return array[start]

    # Step 6: If not sorted, use binary search to find the minimum in the rotated array.
    return find_min_rotated_binary_search(array, start, end)