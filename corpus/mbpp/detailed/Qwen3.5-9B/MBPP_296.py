from typing import List, Tuple

def _merge_sort_and_count(arr: List[int], temp: List[int], left: int, mid: int, right: int) -> int:
    """
    Merge two sorted subarrays and count split inversions.

    Parameters:
        arr: The original list (treated as read-only here; temp is used for merging).
        temp: A temporary list of the same length as arr for merging.
        left: The left index of the subarray (inclusive).
        mid: The midpoint of the subarray (exclusive for left part, inclusive for right part boundary).
        right: The right index of the subarray (inclusive).

    Returns:
        The number of inversions found in the range [left, right].
    """
    i = left      # Pointer for the left subarray
    j = mid + 1   # Pointer for the right subarray
    k = left      # Pointer for the temp array
    split_inversions = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            # arr[i] > arr[j] => inversion because left subarray is sorted
            # All remaining elements in the left subarray (from i to mid)
            # form an inversion with arr[j].
            temp[k] = arr[j]
            split_inversions += (mid - i + 1)
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    # Copy merged elements back to original array
    for idx in range(left, right + 1):
        arr[idx] = temp[idx]

    return split_inversions


def _count_inversions_recursive(arr: List[int], temp: List[int]) -> int:
    """
    Recursively count inversions using merge sort.

    Parameters:
        arr: The list to sort and count inversions for (modified in-place during recursion).
        temp: Pre-allocated temporary list for merging.

    Returns:
        Total number of inversions in the array.
    """
    n = len(arr)

    if n <= 1:
        return 0

    mid = n // 2

    left_count = _count_inversions_recursive(arr, temp)
    right_count = _count_inversions_recursive(arr[mid:], temp)  # Note: passing slice requires care; we handle below properly

    # Since slicing creates a new list, we must avoid creating new lists recursively
    # Instead, we pass indices to the main function logic. 
    # However, to keep helper clean, we will refactor to index-based approach below.
    # For now, this placeholder indicates logic exists but will be implemented in main function.
    return left_count + right_count


def get_Inv_Count(arr: List[int], n: int) -> int:
    """
    Count the number of inversions in the given array.

    An inversion is a pair of indices (i, j) such that:
        i < j and arr[i] > arr[j].

    Parameters:
        arr: List of integers to analyze.
        n: Expected length of the array. Should match len(arr).

    Returns:
        Integer representing the total number of inversions.

    Raises:
        ValueError: If input validation fails.
    """
    # --- Input Validation ---
    if arr is None:
        raise ValueError("Input array 'arr' cannot be None.")
    if not isinstance(arr, list):
        raise TypeError(f"Input 'arr' must be a list, got {type(arr).__name__}.")

    if n is None:
        raise ValueError("Expected length 'n' cannot be None.")
    if not isinstance(n, int):
        raise TypeError(f"Expected length 'n' must be an integer, got {type(n).__name__}.")

    actual_length = len(arr)
    if actual_length != n:
        raise ValueError(
            f"Mismatch between provided length {n} and actual array length {actual_length}."
        )
    if actual_length < 0:
        raise ValueError(f"Array length cannot be negative. Got {actual_length}.")

    # --- Edge Cases ---
    if actual_length == 0:
        return 0

    # Create a working copy to avoid modifying the original list if unintended
    # Although the problem doesn't forbid modification, defensive coding suggests it.
    working_array = list(arr)

    # Allocate temporary array for merge sort operations
    # Its size must match the working array
    temp_array = [0] * actual_length

    # Perform inversion counting using merge sort
    # We implement the index-based version directly to avoid slicing overhead and complexity
    return _merge_sort_with_indices(working_array, temp_array, 0, actual_length - 1)


def _merge_sort_with_indices(arr: List[int], temp: List[int], left: int, right: int) -> int:
    """
    Helper function to recursively sort and count inversions using indices.

    Parameters:
        arr: The array being sorted (modified in-place).
        temp: Temporary buffer for merging.
        left: Left boundary index (inclusive).
        right: Right boundary index (inclusive).

    Returns:
        Number of inversions found in the range [left, right].
    """
    if left >= right:
        # Base case: 0 or 1 element has no inversions
        return 0

    mid = (left + right) // 2

    # Count inversions in left subarray
    left_count = _merge_sort_with_indices(arr, temp, left, mid)

    # Count inversions in right subarray
    right_count = _merge_sort_with_indices(arr, temp, mid + 1, right)

    # Count split inversions and merge
    split_count = _merge_and_count_split_inv(arr, temp, left, mid, right)

    return left_count + right_count + split_count


def _merge_and_count_split_inv(arr: List[int], temp: List[int], left: int, mid: int, right: int) -> int:
    """
    Merge two sorted subarrays [left...mid] and [mid+1...right]
    and count split inversions.

    Parameters:
        arr: The array containing sorted subarrays.
        temp: Temporary array for merging.
        left: Start index of the combined range.
        mid: End index of the left subarray.
        right: End index of the right subarray.

    Returns:
        Number of inversions across the two subarrays.
    """
    i = left
    j = mid + 1
    k = left
    split_inversions = 0

    # Compare elements from both subarrays
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            # arr[i] > arr[j] implies inversion
            # Since left part is sorted, all elements from arr[i] to arr[mid]
            # are greater than arr[j].
            temp[k] = arr[j]
            split_inversions += (mid - i + 1)
            j += 1
        k += 1

    # Copy remaining elements from left subarray
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    # Copy remaining elements from right subarray
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    # Copy merged result back to original array
    for idx in range(left, right + 1):
        arr[idx] = temp[idx]

    return split_inversions