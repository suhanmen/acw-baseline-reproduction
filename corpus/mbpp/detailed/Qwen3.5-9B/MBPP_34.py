from typing import List, Optional, Union

Number = Union[int, float]

def _validate_input_numbers(numbers: List[Number]) -> None:
    """
    Validates that the provided list contains only numeric types.

    This function checks each element in the list to ensure it is either
    an integer or a float. If any element fails this check, a TypeError
    is raised with a descriptive message.

    Args:
        numbers: A list of elements to be validated.

    Raises:
        TypeError: If any element in the list is not a number.
    """
    if not isinstance(numbers, list):
        raise TypeError(f"Expected a list of numbers, but received type: {type(numbers).__name__}")

    for index, item in enumerate(numbers):
        if not isinstance(item, (int, float)):
            raise TypeError(
                f"Element at index {index} is not a number. "
                f"Found type: {type(item).__name__}"
            )


def _validate_sorted_array(numbers: List[Number]) -> None:
    """
    Validates that the provided list is sorted in non-decreasing order.

    This function iterates through the list once, comparing each element
    with its predecessor. If any element is strictly less than the previous
    one, a ValueError is raised.

    Args:
        numbers: A list of numbers to check for sorting order.

    Raises:
        ValueError: If the list is not sorted in non-decreasing order.
    """
    if len(numbers) < 2:
        return

    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:
            raise ValueError(
                f"Array is not sorted. Element at index {i} ({numbers[i]}) "
                f"is less than the previous element ({numbers[i-1]})."
            )


def _validate_array_structure(numbers: List[Number]) -> None:
    """
    Validates the structural requirements of the array for this specific problem.

    Requirements checked:
    1. The array must not be empty (at least 2 elements are needed to define a gap).
    2. All elements must be non-negative (based on the problem context of finding
       a missing number in a sequence starting from 1, though the example allows
       for general gaps, the problem implies a sequence like 1,2,3,5 where 4 is missing.
       If the sequence starts at 1 and is continuous except for one missing number,
       the first element should be 1. However, to be robust against any missing
       number in a strictly increasing integer sequence, we will check for integer
       types specifically if we assume integers only, but the signature accepts
       floats. Given the examples are integers, we will enforce that if the list
       is empty or too short, an error is raised).

    For this specific problem logic (finding a single missing number in a sorted
    sequence where gaps are expected to be 1), we require:
    - At least 2 elements.
    - The elements must be integers (based on the provided assertions).

    Args:
        numbers: The list to validate structure.

    Raises:
        ValueError: If the list is empty or has fewer than 2 elements.
        TypeError: If the list contains non-integer values (assuming integer domain).
    """
    if len(numbers) < 2:
        raise ValueError(
            "The input array must contain at least 2 elements to determine a missing number."
        )

    # Enforce integer type based on problem examples and typical "missing number" context
    for i, item in enumerate(numbers):
        if isinstance(item, float) and not item.is_integer():
            raise TypeError(f"Non-integer float found at index {i}: {item}")
        if isinstance(item, float):
            item = int(item)
        elif not isinstance(item, int):
            raise TypeError(f"Expected integer, found {type(item).__name__} at index {i}")

        numbers[i] = item


def _find_missing_number(numbers: List[int]) -> int:
    """
    Finds the single missing number in a sorted array of integers.

    Assumptions based on problem description:
    - The array is sorted.
    - The array contains consecutive integers except for exactly one missing number.
    - The sequence generally starts at 1 (implied by examples), but the logic
      works for any consecutive sequence provided the gap is size 1.

    Algorithm:
    1. Iterate through the array starting from the second element.
    2. Check if the current element is exactly one greater than the previous.
    3. If not, the missing number is the previous element + 1.
    4. If the loop completes without finding a gap, check if the missing number
       is at the end of the sequence (i.e., after the last element).

    Args:
        numbers: A sorted list of unique integers with exactly one missing number.

    Returns:
        The missing integer.
    """
    missing_value: Optional[int] = None

    # Iterate through the list to find the first gap where difference is not 1
    for i in range(1, len(numbers)):
        expected_value = numbers[i - 1] + 1
        actual_value = numbers[i]

        if actual_value != expected_value:
            # We found the gap
            missing_value = expected_value
            break

    # If no gap was found inside the loop, the missing number must be at the end
    # relative to the current maximum in a sequence that should continue.
    # Example: [1, 2, 3] -> missing 4.
    if missing_value is None:
        missing_value = numbers[-1] + 1

    return missing_value


def find_missing(numbers: List[Number]) -> Number:
    """
    Finds the missing number in a sorted array of integers.

    This function performs rigorous input validation before attempting to
    compute the missing number. It handles edge cases such as empty lists,
    single-element lists, non-numeric inputs, and unsorted arrays.

    Args:
        numbers: A list of numbers representing a sorted sequence with one missing value.

    Returns:
        The missing number in the sequence.

    Raises:
        TypeError: If the input is not a list, contains non-numeric values, 
                   or contains non-integer floats.
        ValueError: If the list is empty, has fewer than 2 elements, or is not sorted.
    """
    # Step 1: Validate that the input is a list
    _validate_input_numbers(numbers)

    # Step 2: Validate that the array is sorted
    _validate_sorted_array(numbers)

    # Step 3: Validate structure (length and integer type)
    _validate_array_structure(numbers)

    # Step 4: Calculate the missing number
    result = _find_missing_number(numbers)

    return result