from typing import List, Any, Union

InputIterable = List[Union[int, float, str]]

def _validate_list_of_elements(elements: InputIterable) -> None:
    """
    Validates that the input is a list where each element is either an int, float, or str.
    Raises a TypeError if validation fails.
    """
    if not isinstance(elements, list):
        raise TypeError(f"Input must be a list, but got {type(elements).__name__}")

    for index, item in enumerate(elements):
        is_valid = isinstance(item, (int, float, str))
        if not is_valid:
            raise TypeError(
                f"All elements in the list must be int, float, or str. "
                f"Invalid element found at index {index}: {type(item).__name__} ({item})"
            )

def _validate_string_input(elements) -> None:
    """
    Validates that the input is a string.
    Raises a TypeError if validation fails.
    """
    if not isinstance(elements, str):
        raise TypeError(f"Input must be a string, but got {type(elements).__name__}")

def _is_integer(val: Any) -> bool:
    """
    Helper to check if a number is effectively an integer (no fractional part).
    """
    return isinstance(val, int) or (isinstance(val, float) and val.is_integer())

def _get_run_length_encoding(input_data: InputIterable) -> List[List[Any]]:
    """
    Core logic to perform run-length encoding on the input data.

    Returns a list of pairs: [count, value].
    """
    result: List[List[Any]] = []

    # Handle empty list edge case explicitly
    if len(input_data) == 0:
        return result

    current_value = input_data[0]
    current_count = 1

    # Iterate through the rest of the list starting from the second element
    for i in range(1, len(input_data)):
        next_value = input_data[i]

        # Check if the current value is the same as the next value
        if current_value == next_value:
            current_count += 1
        else:
            # Append the completed run to the result
            result.append([current_count, current_value])

            # Reset for the new run
            current_value = next_value
            current_count = 1

    # Append the final run after the loop completes
    result.append([current_count, current_value])

    return result

def _prepare_string_input(input_data: str) -> List[Union[int, float, str]]:
    """
    Prepares a string input by converting it into a list of its characters.
    This normalizes the input type to match the logic used for lists.
    """
    return list(input_data)

def encode_list(input_data: InputIterable) -> List[List[Any]]:
    """
    Reflects the run-length encoding from a list or a string.

    Args:
        input_data: A list of elements (int, float, str) or a string.

    Returns:
        A list of lists where each inner list is [count, value].

    Raises:
        TypeError: If the input type or element types are invalid.
        ValueError: If the input is None.
    """
    # Check for None explicitly before type checking
    if input_data is None:
        raise ValueError("Input cannot be None")

    # Determine input type and validate
    if isinstance(input_data, str):
        _validate_string_input(input_data)
        data_list = _prepare_string_input(input_data)
    else:
        _validate_list_of_elements(input_data)
        data_list = input_data

    # Execute the core encoding logic
    return _get_run_length_encoding(data_list)