from typing import Any, Tuple, Union


def _validate_tuple_input(data: Any) -> Tuple[Any, ...]:
    """
    Validate that the input is indeed a tuple.

    Raises:
        TypeError: If the input is not a tuple instance.

    Returns:
        The validated tuple.
    """
    if not isinstance(data, tuple):
        raise TypeError(
            f"Input must be a tuple, but got {type(data).__name__} instead."
        )
    return data


def _convert_elements_to_string(elements: Tuple[Any, ...]) -> Tuple[str, ...]:
    """
    Convert all elements within the tuple to their string representations.

    This handles mixed types (e.g., integers, strings, floats) by using 
    the str() built-in function on each element.

    Args:
        elements: A tuple of arbitrary Python objects.

    Returns:
        A new tuple where every element is a string.
    """
    converted_elements = ()
    for element in elements:
        string_representation = str(element)
        converted_elements = converted_elements + (string_representation,)
    return converted_elements


def concatenate_tuple(tuple_data: tuple, delimiter: str = "-") -> str:
    """
    Concatenate each element of a given tuple by the specified delimiter.

    This function performs robust validation on the input, converts all 
    elements to strings explicitly, and then joins them using the provided 
    delimiter. It handles edge cases such as empty tuples and tuples with 
    mixed data types (integers, floats, strings, etc.).

    Args:
        tuple_data: The tuple containing elements to be concatenated.
        delimiter: The string used to separate the elements. Defaults to "-".

    Returns:
        A single string with all tuple elements joined by the delimiter.

    Raises:
        TypeError: If the input is not a tuple or if the delimiter is not a string.
    """

    # Step 1: Validate the primary input structure
    validated_tuple = _validate_tuple_input(tuple_data)

    # Step 2: Validate the delimiter argument
    if not isinstance(delimiter, str):
        raise TypeError(
            f"Delimiter must be a string, but got {type(delimiter).__name__} instead."
        )

    # Step 3: Handle the empty tuple edge case explicitly
    if len(validated_tuple) == 0:
        # An empty tuple concatenated results in an empty string
        return ""

    # Step 4: Convert all elements to strings
    string_elements = _convert_elements_to_string(validated_tuple)

    # Step 5: Join the converted string elements with the delimiter
    result_string = delimiter.join(string_elements)

    return result_string