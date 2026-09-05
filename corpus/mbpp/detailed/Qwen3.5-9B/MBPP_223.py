def _get_element_at_index(sorted_array, index, array_length):
    """
    Safely retrieve an element from a sorted array at a given index.

    This function handles cases where the index might be out of bounds
    by returning a sentinel value (None) instead of raising an IndexError.

    Args:
        sorted_array (list): The input list, expected to be sorted.
        index (int): The index to retrieve.
        array_length (int): The total length of the array (for boundary checks).

    Returns:
        int or None: The element at the index, or None if the index is out of bounds.
    """
    if index < 0:
        return None
    if index >= array_length:
        return None
    return sorted_array[index]


def _count_majority_candidate(sorted_array, candidate, array_length):
    """
    Count the occurrences of a specific candidate element in the sorted array.

    Since the array is sorted, identical elements are contiguous. We can find
    the count by locating the first and last occurrence of the candidate,
    or by performing a binary search for the first and last positions.

    However, for simplicity and robustness with the sorted property, we will
    implement a standard linear scan optimized for sorted data, but strictly
    adhering to the requirement of explicit steps. Given the sorted nature,
    we can actually do better by finding boundaries, but to ensure clarity and
    defensive coding without relying on advanced library functions like bisect,
    we will implement a binary search to find the first and last occurrence.

    Args:
        sorted_array (list): The input list, expected to be sorted.
        candidate (int): The value to count.
        array_length (int): The total length of the array.

    Returns:
        int: The number of times the candidate appears in the array.
    """
    def _find_first_occurrence(left, right, target):
        """Binary search to find the index of the first occurrence of target."""
        result_index = -1

        while left <= right:
            mid = (left + right) // 2
            current_value = _get_element_at_index(sorted_array, mid, array_length)

            if current_value is None:
                # This shouldn't happen if left/right are within bounds, but safety first
                break

            if current_value == target:
                result_index = mid
                # Try to find an earlier occurrence
                right = mid - 1
            elif current_value < target:
                left = mid + 1
            else:
                # current_value > target
                right = mid - 1

        return result_index

    def _find_last_occurrence(left, right, target):
        """Binary search to find the index of the last occurrence of target."""
        result_index = -1

        while left <= right:
            mid = (left + right) // 2
            current_value = _get_element_at_index(sorted_array, mid, array_length)

            if current_value is None:
                break

            if current_value == target:
                result_index = mid
                # Try to find a later occurrence
                left = mid + 1
            elif current_value < target:
                left = mid + 1
            else:
                # current_value > target
                right = mid - 1

        return result_index

    # Determine initial search range
    search_start = 0
    search_end = array_length - 1

    first_occurrence_index = _find_first_occurrence(search_start, search_end, candidate)

    if first_occurrence_index == -1:
        # Candidate not found in the array
        return 0

    last_occurrence_index = _find_last_occurrence(first_occurrence_index, search_end, candidate)

    if last_occurrence_index == -1:
        # This case is theoretically unreachable if first_occurrence was found
        return 0

    count = last_occurrence_index - first_occurrence_index + 1
    return count


def _calculate_required_majority_count(array_length):
    """
    Calculate the minimum number of occurrences required for a majority element.

    A majority element is defined as an element that appears more than n/2 times.

    Args:
        array_length (int): The length of the array.

    Returns:
        int: The threshold count needed to be a majority.
    """
    if array_length <= 0:
        return 0
    return (array_length // 2) + 1


def _validate_inputs(sorted_array, array_length, candidate):
    """
    Validate the inputs against the problem constraints and types.

    Args:
        sorted_array (list): The input list.
        array_length (int): The expected length of the list.
        candidate (int): The candidate element to check.

    Raises:
        TypeError: If inputs are not of expected types.
        ValueError: If array length mismatches actual list length or other logical errors.
    """
    # Check type of sorted_array
    if not isinstance(sorted_array, list):
        raise TypeError("sorted_array must be a list.")

    # Check type of array_length
    if not isinstance(array_length, int):
        raise TypeError("array_length must be an integer.")

    # Check type of candidate
    if not isinstance(candidate, int):
        raise TypeError("candidate must be an integer.")

    # Check actual length matches declared length
    actual_length = len(sorted_array)
    if actual_length != array_length:
        raise ValueError(f"Declared array_length ({array_length}) does not match actual list length ({actual_length}).")

    # Check for negative length
    if array_length < 0:
        raise ValueError("array_length cannot be negative.")

    # Check if array is actually sorted (defensive programming)
    # Although the problem states it is sorted, we validate it for robustness
    for i in range(1, actual_length):
        if sorted_array[i] < sorted_array[i-1]:
            raise ValueError("The provided array must be sorted in non-decreasing order.")


def is_majority(sorted_array, array_length, candidate):
    """
    Check if a specific candidate is a majority element in a sorted array.

    A majority element is an element that appears strictly more than floor(n/2) times.

    Args:
        sorted_array (list): The sorted list of integers.
        array_length (int): The length of the list (should be len(sorted_array)).
        candidate (int): The integer value to check for majority status.

    Returns:
        bool: True if the candidate is a majority element, False otherwise.

    Raises:
        TypeError: If input types are incorrect.
        ValueError: If input lengths mismatch or array is not sorted.
    """
    # Step 1: Validate all inputs
    _validate_inputs(sorted_array, array_length, candidate)

    # Handle edge case: empty array
    if array_length == 0:
        # Cannot have a majority in an empty set
        return False

    # Step 2: Calculate the required threshold for a majority
    required_count = _calculate_required_majority_count(array_length)

    # Step 3: Count occurrences of the candidate in the sorted array
    occurrence_count = _count_majority_candidate(sorted_array, candidate, array_length)

    # Step 4: Compare count against threshold
    is_majority_status = occurrence_count > required_count

    return is_majority_status