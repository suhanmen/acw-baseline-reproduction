from typing import List

def get_Inv_Count(arr: List[int], n: int) -> int:
    """
    Calculates the number of inversions in an array.
    An inversion is a pair (i, j) such that i < j and arr[i] > arr[j].

    Complexity: O(n log n) time, O(n) space.
    This implementation uses a Merge Sort based approach.
    """
    # Input Validation
    if not isinstance(arr, list):
        raise TypeError("Input 'arr' must be a list of integers.")
    if not isinstance(n, int):
        raise TypeError("Input 'n' must be an integer.")

    # Checking consistency between the list length and n
    if len(arr) != n:
        raise ValueError(f"The length of the array ({len(arr)}) does not match n ({n}).")

    # Handle edge cases: empty list or single element
    if n <= 1:
        return 0

    # We work on a copy to avoid mutating the original list passed by the user
    working_arr = list(arr)

    # The core logic uses a recursive merge sort that counts swaps
    total_inversions = _merge_sort_and_count(working_arr, 0, n - 1)

    return total_inversions

def _merge_sort_and_count(arr: List[int], left_index: int, right_index: int) -> int:
    """
    Recursively divides the array and sums inversions from sub-problems 
    and the merge step.
    """
    inversion_count = 0

    # Base case: if the range contains one or zero elements
    if left_index >= right_index:
        return 0

    # Find the midpoint to split the array into two halves
    mid_point = (left_index + right_index) // 2

    # Recursively count inversions in the left half
    left_count = _merge_sort_and_count(arr, left_index, mid_point)
    inversion_count += left_count

    # Recursively count inversions in the right half
    right_count = _merge_sort_and_count(arr, mid_point + 1, right_index)
    inversion_count += right_count

    # Count cross-inversions during the merge step
    merge_count = _merge_and_count_cross_inversions(arr, left_index, mid_point, right_index)
    inversion_count += merge_count

    return inversion_count

def _merge_and_count_cross_inversions(arr: List[int], left: int, mid: int, right: int) -> int:
    """
    Merges two sorted sub-arrays and counts how many times an element 
    from the right sub-array is smaller than an element from the left.
    """
    # Create temporary lists to hold the divided parts
    left_part = []
    for i in range(left, mid + 1):
        left_part.append(arr[i])

    right_part = []
    for j in range(mid + 1, right + 1):
        right_part.append(arr[j])

    i_ptr = 0  # Pointer for left_part
    j_ptr = 0  # Pointer for right_part
    k_ptr = left  # Pointer for the original array being updated
    cross_inversions = 0

    # Standard merge process with inversion counting logic
    while i_ptr < len(left_part) and j_ptr < len(right_part):
        if left_part[i_ptr] <= right_part[j_ptr]:
            # Element is in correct order
            arr[k_ptr] = left_part[i_ptr]
            i_ptr += 1
        else:
            # Inversion detected: left_part[i_ptr] > right_part[j_ptr]
            # Since left_part is sorted, all remaining elements in left_part 
            # are also greater than right_part[j_ptr].
            arr[k_ptr] = right_part[j_ptr]

            # Number of elements remaining in left_part starting from i_ptr
            num_elements_left = len(left_part) - i_ptr
            cross_inversions += num_elements_left

            j_ptr += 1

        k_ptr += 1

    # Copy any remaining elements from left_part
    while i_ptr < len(left_part):
        arr[k_ptr] = left_part[i_ptr]
        i_ptr += 1
        k_ptr += 1

    # Copy any remaining elements from right_part
    while j_ptr < len(right_part):
        arr[k_ptr] = right_part[j_ptr]
        j_ptr += 1
        k_ptr += 1

    return cross_inversions