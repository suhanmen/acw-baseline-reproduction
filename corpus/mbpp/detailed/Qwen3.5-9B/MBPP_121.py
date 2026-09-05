from typing import List, Optional, Tuple

def _validate_numeric_value(value, index: int, param_name: str) -> None:
    """
    Validates that a given value is a finite number (int or float).

    :param value: The value to check.
    :param index: The index/position of the value in the input (for error messages).
    :param param_name: The name of the parameter for error messages.
    :raises TypeError: If the value is not a number.
    :raises ValueError: If the value is not finite.
    """
    if not isinstance(value, (int, float)):
        raise TypeError(
            f"Parameter '{param_name}' contains invalid type at position {index}: expected int or float, got {type(value).__name__}."
        )
    if not (value == value):  # Check for NaN (NaN != NaN is True)
        raise ValueError(
            f"Parameter '{param_name}' contains non-finite number at position {index}: got NaN."
        )


def _validate_list_input(array, param_name: str = "array") -> List:
    """
    Validates that the input is a list or tuple of numeric values.

    :param array: The input sequence to validate.
    :param param_name: The name of the parameter for error messages.
    :raises TypeError: If the input is not a list or tuple.
    :raises ValueError: If the list is empty or contains invalid elements.
    :return: A copy of the validated list.
    """
    if not isinstance(array, (list, tuple)):
        raise TypeError(
            f"Parameter '{param_name}' must be a list or tuple, got {type(array).__name__}."
        )

    if len(array) == 0:
        raise ValueError(f"Parameter '{param_name}' cannot be empty.")

    validated_list = []
    for i, value in enumerate(array):
        _validate_numeric_value(value, i, param_name)
        validated_list.append(value)

    return validated_list


def _get_third_value(target_sum: int, first_val: float, second_val: float) -> Optional[float]:
    """
    Calculates the required third value to meet the target sum.

    :param target_sum: The desired total sum.
    :param first_val: The value of the first element.
    :param second_val: The value of the second element.
    :return: The calculated third value, or None if values are infinite/invalid.
    """
    current_sum = first_val + second_val

    # Handle potential infinity cases
    if current_sum != current_sum:  # Check for NaN
        return None

    return target_sum - current_sum


def _find_triplet_in_array(
    array: List[float], 
    target_sum: int, 
    first_idx: int,
    second_idx: int
) -> Optional[Tuple[int, int, int]]:
    """
    Searches for a third element in the array that, when added to the first two,
    equals the target sum.

    :param array: The list of numbers.
    :param target_sum: The desired sum.
    :param first_idx: The index of the first number.
    :param second_idx: The index of the second number.
    :return: A tuple of (first_idx, second_idx, third_idx) if found, None otherwise.
    """
    first_val = array[first_idx]
    second_val = array[second_idx]

    required_third = _get_third_value(target_sum, first_val, second_val)

    if required_third is None:
        return None

    # Check remaining elements for the required third value
    # We skip indices first_idx and second_idx to ensure distinct elements
    remaining_indices = []
    for i in range(len(array)):
        if i == first_idx or i == second_idx:
            continue
        remaining_indices.append(i)

    for idx in remaining_indices:
        if abs(array[idx] - required_third) < 1e-9:  # Handle float comparison
            return (first_idx, second_idx, idx)

    return None


def check_triplet(
    array: List,
    target_sum: int,
    first_index: int,
    second_index: int
) -> bool:
    """
    Checks if there exists a triplet in the given array such that:
    1. The first two elements are at the specified indices (first_index and second_index).
    2. A third element exists at a different index.
    3. The sum of these three elements equals target_sum.

    :param array: List of numbers.
    :param target_sum: The target sum for the triplet.
    :param first_index: Index of the first element in the triplet.
    :param second_index: Index of the second element in the triplet.
    :return: True if a valid triplet exists, False otherwise.
    :raises TypeError: If inputs are not of expected types.
    :raises ValueError: If indices are out of bounds or if no valid triplet is found.
    """

    # Validate input types and contents
    validated_array = _validate_list_input(array)

    # Validate target_sum is a number
    _validate_numeric_value(target_sum, -1, "target_sum")

    # Validate first_index
    if not isinstance(first_index, (int, float)):
        raise TypeError(f"Parameter 'first_index' must be an integer, got {type(first_index).__name__}.")
    first_index = int(first_index)
    if first_index < 0 or first_index >= len(validated_array):
        raise ValueError(
            f"Parameter 'first_index' is out of bounds: {first_index} is not in range [0, {len(validated_array)-1}]."
        )

    # Validate second_index
    if not isinstance(second_index, (int, float)):
        raise TypeError(f"Parameter 'second_index' must be an integer, got {type(second_index).__name__}.")
    second_index = int(second_index)
    if second_index < 0 or second_index >= len(validated_array):
        raise ValueError(
            f"Parameter 'second_index' is out of bounds: {second_index} is not in range [0, {len(validated_array)-1}]."
        )

    # Check if indices are distinct
    if first_index == second_index:
        raise ValueError("Parameters 'first_index' and 'second_index' must be distinct.")

    # Attempt to find the triplet
    result = _find_triplet_in_array(validated_array, target_sum, first_index, second_index)

    if result is None:
        return False

    # If we found a valid triplet, verify it explicitly one more time for clarity
    _, _, third_idx = result

    # Ensure third index is also valid and distinct
    if third_idx == first_index or third_idx == second_index:
        return False

    sum_check = (
        validated_array[first_index] + 
        validated_array[second_index] + 
        validated_array[third_idx]
    )

    # Check if sum matches target (using tolerance for floats)
    if isinstance(target_sum, float):
        return abs(sum_check - target_sum) < 1e-9

    return sum_check == target_sum