from typing import Tuple, List, Union

# Define the type hint for the input argument
InputTuple = Tuple[Union[str, int, float], ...]

def validate_input_tuple(tup: InputTuple) -> InputTuple:
    """
    Validates that the input is a tuple and contains only strings or numeric types.
    Returns the validated tuple if successful, otherwise raises a TypeError.
    """
    if not isinstance(tup, tuple):
        raise TypeError(f"Input must be a tuple, got {type(tup).__name__} instead.")

    for i, item in enumerate(tup):
        if not isinstance(item, (str, int, float)):
            raise TypeError(
                f"All elements in the tuple must be strings, integers, or floats. "
                f"Element at index {i} is of type {type(item).__name__}."
            )

    return tup

def convert_element_to_string(element: Union[str, int, float]) -> str:
    """
    Converts a single element (string, int, or float) to its string representation.
    """
    if isinstance(element, str):
        return element
    elif isinstance(element, (int, float)):
        return str(element)
    else:
        # This case should ideally be caught by validation, but added for defense
        return f"<unsupported_type:{type(element).__name__}>"

def construct_result_string(elements: List[str], separator: str) -> str:
    """
    Joins a list of string elements into a single result string.
    """
    if not elements:
        return ""

    result_parts: List[str] = []

    for item in elements:
        result_parts.append(item)

    # Use join to efficiently concatenate strings
    return separator.join(result_parts)

def tup_string(input_tuple: InputTuple) -> str:
    """
    Converts a tuple of strings (or numbers) into a single concatenated string.

    The function treats elements as items to be concatenated directly without separators.
    For example: ('e', 'x') -> "ex"

    Args:
        input_tuple: A tuple containing strings or numeric values.

    Returns:
        A single string formed by concatenating all elements in the tuple.

    Raises:
        TypeError: If the input is not a tuple or contains invalid element types.

    Examples:
        >>> tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's'))
        'exercises'
        >>> tup_string(('p','y','t','h','o','n'))
        'python'
    """
    # Step 1: Validate the input type and contents
    validated_tuple = validate_input_tuple(input_tuple)

    # Step 2: Determine if the tuple is empty
    if len(validated_tuple) == 0:
        return ""

    # Step 3: Initialize a list to hold converted string parts
    string_parts: List[str] = []

    # Step 4: Iterate through each element in the validated tuple
    for item in validated_tuple:
        # Convert the current item to a string explicitly
        string_representation = convert_element_to_string(item)
        # Append the string representation to the list of parts
        string_parts.append(string_representation)

    # Step 5: Join all string parts into a single result string
    # The separator is an empty string to concatenate elements directly
    final_string = construct_result_string(string_parts, "")

    return final_string