def _is_sorted_list_increasing_unique(sorted_list: list) -> bool:
    """
    Check if a list is sorted in strictly increasing order.

    This function validates that:
    1. The list is non-empty.
    2. Each element is an integer.
    3. Each element is strictly greater than the previous one.

    Args:
        sorted_list (list): The list to validate.

    Returns:
        bool: True if the list is sorted in strictly increasing order, False otherwise.
    """
    # Handle edge case: empty list
    if not sorted_list:
        return False

    # Validate that the list contains integers only
    for index, value in enumerate(sorted_list):
        if not isinstance(value, int):
            return False

    # Iterate through the list to check for strictly increasing order
    # We skip the first element in the range since it has no predecessor to compare with
    for current_index in range(1, len(sorted_list)):
        previous_value = sorted_list[current_index - 1]
        current_value = sorted_list[current_index]

        # Check if current value is strictly greater than previous value
        if current_value <= previous_value:
            return False

    return True


def _get_min_max(values: list) -> tuple:
    """
    Calculate the minimum and maximum values from a list.

    Args:
        values (list): The list of numbers.

    Returns:
        tuple: A tuple containing (min_value, max_value).
    """
    if not values:
        # Should not happen if input validation is done upstream, but handled defensively
        return (float('inf'), float('-inf'))

    min_val = values[0]
    max_val = values[0]

    for value in values:
        if value < min_val:
            min_val = value
        if value > max_val:
            max_val = value

    return (min_val, max_val)


def check_Consecutive(input_list) -> bool:
    """
    Check whether the given list contains consecutive numbers.

    Consecutive numbers are defined as a sequence where:
    1. All elements are integers.
    2. The list contains no duplicates.
    3. The difference between the maximum and minimum element equals the count of elements minus one.
    4. The list can be sorted into a strictly increasing sequence where each step is +1.

    Note: The problem implies checking if the numbers form a consecutive sequence regardless of order.
    Examples:
        [1, 2, 3, 4, 5] -> True
        [5, 3, 4, 1, 2] -> True (permutation of consecutive numbers)
        [1, 2, 3, 5, 6] -> False
        [1, 2, 1] -> False (contains duplicate)

    Args:
        input_list (list): The list of numbers to check.

    Returns:
        bool: True if the list contains consecutive numbers, False otherwise.
    """
    # Validate input type
    if not isinstance(input_list, list):
        return False

    # Handle edge case: empty input list
    if len(input_list) == 0:
        return False

    # Handle edge case: single element list
    # A single element is trivially consecutive by definition (sequence of length 1)
    if len(input_list) == 1:
        # Additionally validate it is an integer
        if not isinstance(input_list[0], int):
            return False
        return True

    # Step 1: Validate all elements are integers
    # This handles negative numbers, zeros, and ensures no floats or strings slip through
    for element in input_list:
        if not isinstance(element, int):
            return False

    # Step 2: Create a copy of the list to sort without mutating the original
    sorted_values = input_list.copy()

    # Step 3: Sort the list in ascending order
    sorted_values.sort()

    # Step 4: Check for duplicates in the sorted list
    # If any element equals its next neighbor, there are duplicates
    has_duplicates = False
    for index in range(1, len(sorted_values)):
        if sorted_values[index] == sorted_values[index - 1]:
            has_duplicates = True
            break

    if has_duplicates:
        return False

    # Step 5: Verify the list is strictly increasing (redundant check after duplicate check, but explicit for clarity)
    if not _is_sorted_list_increasing_unique(sorted_values):
        return False

    # Step 6: Check if the numbers are consecutive
    # For consecutive integers, the difference between max and min must equal (count - 1)
    min_val, max_val = _get_min_max(sorted_values)
    count = len(sorted_values)

    expected_range_span = count - 1
    actual_range_span = max_val - min_val

    if actual_range_span != expected_range_span:
        return False

    # If all checks pass, the list contains consecutive numbers
    return True