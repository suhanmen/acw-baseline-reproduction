from typing import List, Any, Tuple

def _validate_input(data: List[Any]) -> Tuple[List[Any], bool]:
    """
    Validates the input list.

    Returns:
        A tuple containing:
        - The validated list (as a copy to avoid modifying the original).
        - A boolean indicating if the validation passed.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-hashable elements in a way that 
                    would cause issues for standard operations (though we accept any iterable here,
                    we enforce it's a list as per typical use cases for this problem).
    """
    if not isinstance(data, list):
        raise TypeError("Input must be a list.")

    # We accept any length, including empty lists, as valid inputs.
    # The logic handles empty lists gracefully.
    return list(data), True

def _extract_non_zeroes(numbers: List[Any]) -> List[Any]:
    """
    Extracts all non-zero elements from the list while preserving their order.

    Args:
        numbers: A list of elements.

    Returns:
        A new list containing only the non-zero elements.
    """
    non_zero_elements: List[Any] = []

    for element in numbers:
        # Check if the element is not equal to 0.
        # We use '0' explicitly as the target value for zeroing.
        if element != 0:
            non_zero_elements.append(element)

    return non_zero_elements

def _count_zeroes(numbers: List[Any]) -> int:
    """
    Counts the number of zero elements in the list.

    Args:
        numbers: A list of elements.

    Returns:
        The integer count of zeros found in the list.
    """
    zero_count: int = 0

    for element in numbers:
        if element == 0:
            zero_count += 1

    return zero_count

def _construct_result(non_zeroes: List[Any], zero_count: int) -> List[Any]:
    """
    Constructs the final list by appending the correct number of zeros
    to the end of the non-zero elements list.

    Args:
        non_zeroes: A list of non-zero elements.
        zero_count: The number of zeros to append.

    Returns:
        The final reordered list.
    """
    # Start with a copy of the non-zero elements to ensure immutability of the caller's data logic
    result: List[Any] = list(non_zeroes)

    # Append the calculated number of zeros
    for _ in range(zero_count):
        result.append(0)

    return result

def re_order(data: List[Any]) -> List[Any]:
    """
    Moves all zeroes to the end of the given array.
    The relative order of non-zero elements is preserved.

    Args:
        data: A list of elements.

    Returns:
        A new list with all zeroes moved to the end.

    Raises:
        TypeError: If the input is not a list.

    Edge Cases Handled:
        - Empty list: Returns an empty list.
        - List with no zeroes: Returns the original list.
        - List with all zeroes: Returns a list of zeroes.
        - Single element: Returns the element unchanged (if not zero) or [0] (if zero).
        - Mixed types: Handles any type as long as equality with 0 can be checked.
    """
    # Step 1: Validate input and create a working copy
    validated_data, is_valid = _validate_input(data)

    if not is_valid:
        raise TypeError("Input validation failed.")

    # Edge Case: Empty list
    if len(validated_data) == 0:
        return []

    # Step 2: Extract non-zero elements
    non_zero_elements = _extract_non_zeroes(validated_data)

    # Step 3: Count the total number of zeroes
    zero_count = _count_zeroes(validated_data)

    # Step 4: Construct the final result
    final_result = _construct_result(non_zero_elements, zero_count)

    return final_result