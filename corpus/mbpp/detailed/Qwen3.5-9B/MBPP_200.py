from typing import List, Union

def _validate_list_input(value: Union[int, float, str, List, None]) -> List[int]:
    """
    Validates that the input is a list of numbers (int or float).
    Raises a TypeError if the validation fails.
    """
    if not isinstance(value, list):
        raise TypeError(f"Input must be a list, but got: {type(value).__name__}")

    if len(value) == 0:
        raise ValueError("Input list cannot be empty.")

    for i, element in enumerate(value):
        if not isinstance(element, (int, float)):
            raise TypeError(f"All elements must be numbers. Element at index {i} is of type: {type(element).__name__}")
        # Check for non-finite float values (inf, -inf, nan)
        if isinstance(element, float):
            if element != element:  # NaN check
                raise ValueError(f"List contains NaN at index {i}.")
            if element == float('inf') or element == float('-inf'):
                raise ValueError(f"List contains infinity at index {i}.")

    return value


def _find_maximum_value(numbers: List[Union[int, float]]) -> Union[int, float]:
    """
    Finds the maximum value in a non-empty list of numbers.
    """
    current_max = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] > current_max:
            current_max = numbers[i]

    return current_max


def position_max(numbers: Union[int, float, str, List]) -> List[int]:
    """
    Finds all index positions of the maximum values in a given list.

    Parameters:
    numbers (list): A list of numeric values (int or float).

    Returns:
    list: A list of integer indices where the maximum value occurs.

    Raises:
    TypeError: If input is not a list or contains non-numeric elements.
    ValueError: If the list is empty or contains invalid numeric values (inf, nan).
    """
    # Step 1: Validate the input structure and content
    validated_input = _validate_list_input(numbers)

    # Step 2: Retrieve the maximum value from the validated list
    max_value = _find_maximum_value(validated_input)

    # Step 3: Collect all indices where the element equals the maximum value
    max_indices = []
    for index in range(len(validated_input)):
        # Use a direct comparison. Since we validated against inf/nan, this is safe.
        if validated_input[index] == max_value:
            max_indices.append(index)

    return max_indices