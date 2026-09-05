def _is_valid_sorted_array_with_bounds(values: list, lower_bound: int, upper_bound: int) -> bool:
    """
    Validates that:
    1. `values` is a list.
    2. `lower_bound` and `upper_bound` are integers.
    3. `lower_bound` <= `upper_bound`.
    4. The length of `values` is exactly (upper_bound - lower_bound + 1).
    5. The array is sorted in non-decreasing order.
    6. All elements are integers.

    Returns True if valid, False otherwise.
    """

    # Check if values is a list
    if not isinstance(values, list):
        return False

    # Check if lower_bound and upper_bound are integers
    if not isinstance(lower_bound, int) or not isinstance(upper_bound, int):
        return False

    # Check bounds order
    if lower_bound > upper_bound:
        return False

    # Calculate expected length
    expected_length = upper_bound - lower_bound + 1
    actual_length = len(values)

    # Check if lengths match
    if actual_length != expected_length:
        return False

    # Check if array is sorted and contains only integers
    for i in range(len(values)):
        current_value = values[i]

        # Check if current element is an integer
        if not isinstance(current_value, int):
            return False

        # Check if array is sorted (non-decreasing)
        if i > 0:
            previous_value = values[i - 1]
            if current_value < previous_value:
                return False

    return True


def _find_smallest_missing_linear(values: list, lower_bound: int, upper_bound: int) -> int:
    """
    Finds the smallest missing element in a sorted array using a linear scan.
    This fallback is used if binary search is not directly applicable or as a sanity check.
    """

    # Iterate through each position in the expected range
    for i in range(lower_bound, upper_bound + 1):
        # Get the value at the current index if it exists
        if i < len(values):
            current_value = values[i]
        else:
            current_value = None

        # If the value at this index does not match the expected index value,
        # then the expected index value is the smallest missing one.
        if current_value != i:
            return i

    # If all positions from lower_bound to upper_bound are filled correctly,
    # then the smallest missing element is upper_bound + 1.
    return upper_bound + 1


def _binary_search_first_mismatch(values: list, lower_bound: int, upper_bound: int) -> int:
    """
    Uses binary search to find the first index where values[index] != index.
    Assumes the array is sorted and contains integers.
    If all elements match their index, returns upper_bound + 1.
    """

    left = lower_bound
    right = upper_bound

    # While the search space is valid
    while left <= right:
        mid = (left + right) // 2

        mid_value = values[mid]

        if mid_value == mid:
            # The element at mid matches its index, so the missing element is to the right
            left = mid + 1
        else:
            # The element at mid does not match its index.
            # Since the array is sorted, this might be the first mismatch.
            # We need to check if there's a mismatch before this index.
            right = mid - 1

    # At the end of the loop, 'left' points to the first index where values[index] != index
    # If left exceeds upper_bound, it means all elements matched their indices.
    if left > upper_bound:
        return upper_bound + 1
    else:
        return left


def smallest_missing(values: list, lower_bound: int, upper_bound: int) -> int:
    """
    Finds the smallest missing element in a sorted array within a specific range.

    The function assumes the array represents a sequence from 'lower_bound' to 'upper_bound',
    where the element at index i (relative to the array start) should ideally be 
    (lower_bound + i). The function finds the first value in this range that is missing.

    Parameters:
    values (list): A sorted list of integers.
    lower_bound (int): The start of the expected range.
    upper_bound (int): The end of the expected range.

    Returns:
    int: The smallest missing element in the range [lower_bound, upper_bound].
         If no element is missing within the range, returns upper_bound + 1.

    Raises:
    TypeError: If input types are incorrect.
    ValueError: If input values or bounds are inconsistent.
    """

    # Step 1: Validate all inputs explicitly
    if not _is_valid_sorted_array_with_bounds(values, lower_bound, upper_bound):
        raise ValueError("Invalid input: values must be a sorted list of integers matching the range defined by lower_bound and upper_bound.")

    # Step 2: Use binary search for efficiency given the sorted nature of the input
    missing_element = _binary_search_first_mismatch(values, lower_bound, upper_bound)

    # Step 3: Return the result
    return missing_element