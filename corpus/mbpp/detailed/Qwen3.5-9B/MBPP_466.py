from typing import List, Optional, Union

Number = Union[int, float]


def _is_valid_input(arr: List[Number], length: int) -> bool:
    """
    Validate that the input list and length parameter are valid.

    Requirements:
    - arr must be a list.
    - length must be a non-negative integer.
    - length must match the actual length of arr.
    """
    if not isinstance(arr, list):
        return False

    if not isinstance(length, int) or isinstance(length, bool):
        return False

    if length < 0:
        return False

    actual_length = len(arr)
    if actual_length != length:
        return False

    return True


def _is_peak_element(
    arr: List[Number],
    index: int,
    length: int
) -> bool:
    """
    Determine if the element at the given index is a peak.

    A peak element is strictly greater than its neighbors.
    Boundary elements only need to be greater than their single neighbor.

    Args:
        arr: The input list of numbers.
        index: The index to check.
        length: The total length of the array (used for boundary checks).

    Returns:
        True if the element at index is a peak, False otherwise.
    """
    # Basic sanity check inside the helper (though validation happens before calling)
    if index < 0 or index >= length:
        return False

    current_value = arr[index]
    is_left_boundary = (index == 0)
    is_right_boundary = (index == length - 1)

    # Check left neighbor if it exists
    if not is_left_boundary:
        left_neighbor = arr[index - 1]
        if current_value <= left_neighbor:
            return False

    # Check right neighbor if it exists
    if not is_right_boundary:
        right_neighbor = arr[index + 1]
        if current_value <= right_neighbor:
            return False

    return True


def find_peak(arr: List[Number], length: int) -> int:
    """
    Find the index of a peak element in the given array.

    A peak element is defined as an element that is strictly greater than its neighbors.
    For boundary elements, they only need to be greater than their single existing neighbor.

    This implementation uses a brute-force linear scan approach for clarity and explicit steps,
    ensuring every comparison is visible and debuggable. It finds the first peak encountered.

    Parameters:
        arr: A list of numbers.
        length: An integer representing the expected length of the array.

    Returns:
        The index of a peak element.

    Raises:
        ValueError: If inputs are invalid (wrong type, negative length, mismatched length).
    """
    # Step 1: Input Validation
    if not _is_valid_input(arr, length):
        raise ValueError(
            f"Invalid input: Expected list of length {length}, "
            f"received list of length {len(arr)} with type {type(arr)}."
        )

    # Step 2: Handle the edge case of empty array or zero length
    # Although _is_valid_input ensures length == len(arr), this makes the intent explicit.
    if length == 0:
        raise ValueError("Cannot find a peak in an empty array.")

    # Step 3: Iterate through each element to find a peak
    # We will search from the first element up to the second-to-last element.
    # Note: Since we validated the length, we can safely access indices 0 to length-1.

    index_found = -1

    # Explicit loop over indices
    for current_index in range(length):
        # Call the helper to check if this index represents a peak
        if _is_peak_element(arr, current_index, length):
            index_found = current_index
            break  # Stop at the first peak found

    # Step 4: Verify that a peak was actually found
    if index_found == -1:
        # In a strictly unimodal or valid mathematical context, a peak is guaranteed.
        # However, for arbitrary arrays where no element is strictly greater than both neighbors
        # (e.g., all equal elements [5, 5, 5]), no strict peak exists.
        raise ValueError(
            "No peak element found in the array where every element is strictly greater "
            "than its neighbors."
        )

    return index_found