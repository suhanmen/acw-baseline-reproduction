from typing import List


def _validate_inputs(arr: List[int], k: int) -> None:
    """
    Validates the input types and constraints.

    Args:
        arr: The input list of integers.
        k: The requested number of maximum elements.

    Raises:
        ValueError: If k is out of the valid range [0, len(arr)].
        TypeError: If arr is not a list or k is not an integer.
    """
    if not isinstance(arr, list):
        raise TypeError(f"Expected input 'arr' to be a list, but got {type(arr).__name__}")

    if not isinstance(k, int):
        raise TypeError(f"Expected input 'k' to be an integer, but got {type(k).__name__}")

    array_length = len(arr)
    if k < 0 or k > array_length:
        raise ValueError(
            f"Input 'k' must be between 0 and {array_length} (inclusive). "
            f"Received k = {k}."
        )

    for index, element in enumerate(arr):
        if not isinstance(element, int):
            raise TypeError(
                f"Element at index {index} is not an integer: {element} ({type(element).__name__})"
            )


def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:
        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:
        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:
        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    # 1. Validate inputs to ensure they meet the specified constraints.
    _validate_inputs(arr, k)

    # 2. Handle the trivial edge case where k is 0.
    if k == 0:
        return []

    # 3. Create a copy of the array to avoid mutating the original input.
    # Production-grade code should generally treat input arguments as immutable.
    working_copy = list(arr)

    # 4. Sort the array in ascending order.
    # Python's Timsort is O(n log n) and stable.
    working_copy.sort()

    # 5. Identify the largest k elements.
    # Since the list is sorted in ascending order, the largest k elements 
    # are located at the end of the list.
    total_elements = len(working_copy)
    start_index = total_elements - k

    # We slice from start_index to the end of the list.
    max_k_elements = working_copy[start_index:]

    # 6. The requirements state to return a sorted list of length k.
    # Our current max_k_elements is already sorted because it is a slice
    # of a sorted list. We confirm its length and return.
    if len(max_k_elements) != k:
        # This point should theoretically be unreachable due to the validation step.
        raise RuntimeError("Internal error: Resulting list length does not match k.")

    return max_k_elements