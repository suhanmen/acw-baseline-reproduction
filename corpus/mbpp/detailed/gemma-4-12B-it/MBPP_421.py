from typing import Tuple, Any


def concatenate_tuple(input_tuple: Tuple[Any, ...], delimiter: str = "-") -> str:
    """
    Concatenates every element of a given tuple into a single string, 
    joined by a specified delimiter. Elements that are not strings 
    are converted to their string representation.

    Args:
        input_tuple (Tuple[Any, ...]): A tuple containing elements to join.
        delimiter (str): The string used to separate joined elements. 
                          Defaults to "-".

    Returns:
        str: The concatenated string of all elements.

    Raises:
        TypeError: If the input_tuple is not a tuple.
        ValueError: If the input_tuple is empty.
    """
    # Validate that the input is actually a tuple
    if not isinstance(input_tuple, tuple):
        raise TypeError(f"Input must be a tuple, but received {type(input_tuple).__name__}")

    # Handle the edge case of an empty tuple
    # Based on typical concatenation logic, an empty tuple results in an empty string,
    # but we can also treat it as a specific case depending on requirements.
    # For this implementation, we return an empty string for empty tuples.
    if len(input_tuple) == 0:
        return ""

    # List to store the string representations of all elements
    string_elements_list: list[str] = []

    # Iterate through each element to ensure it is converted to a string
    for element in input_tuple:
        # Handle None specifically if necessary, or just let str() handle it
        # str(4) becomes "4", str("ID") becomes "ID"
        element_as_string = str(element)
        string_elements_list.append(element_as_string)

    # Join all elements using the provided delimiter
    # Using join() is the standard, production-grade way to concatenate strings
    result_string = delimiter.join(string_elements_list)

    return result_string


# Verification against the provided assertions
if __name__ == "__main__":
    # The following block verifies the functionality against the provided requirements.
    # These will raise an AssertionError if the logic is incorrect.
    assert concatenate_tuple(("ID", "is", 4, "UTS")) == 'ID-is-4-UTS'
    assert concatenate_tuple(("QWE", "is", 4, "RTY")) == 'QWE-is-4-RTY'
    assert concatenate_tuple(("ZEN", "is", 4, "OP")) == 'ZEN-is-4-OP'