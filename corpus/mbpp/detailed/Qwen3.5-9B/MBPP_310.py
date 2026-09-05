def _validate_input(value, type_name: str):
    """
    Validates that the provided value is a string and raises a TypeError otherwise.

    This helper function centralizes validation logic to ensure consistent
    error handling across the main function.

    Args:
        value: The input value to validate.
        type_name: A string descriptor for error messages.

    Returns:
        The validated string value if successful.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(value, str):
        raise TypeError(f"Expected {type_name} but received {type(value).__name__}.")
    return value


def _convert_string_to_characters(s: str):
    """
    Iterates through a string to collect each individual character into a list.

    This function explicitly handles the iteration process to ensure clarity
    and allows for easy modification of the collection mechanism if needed.
    It treats the input as an immutable sequence of characters and converts
    it into a mutable list for subsequent processing.

    Args:
        s: A validated string input.

    Returns:
        A list containing each character of the input string.
    """
    characters = []
    for char in s:
        characters.append(char)
    return characters


def _convert_list_to_tuple(char_list: list):
    """
    Converts a list of characters into a tuple.

    This function performs the final transformation from the mutable list
    collected during iteration to the immutable tuple required by the problem.

    Args:
        char_list: A list of characters derived from the input string.

    Returns:
        A tuple containing the characters from the input string.
    """
    return tuple(char_list)


def string_to_tuple(input_str: str):
    """
    Converts a given string into a tuple of its individual characters.

    This function follows a step-by-step approach to convert the input string:
    1. Validates the input type to ensure it is a string.
    2. Iterates through the string to collect each character explicitly.
    3. Converts the resulting list of characters into a tuple.

    Edge cases handled include:
    - Empty strings (returns an empty tuple).
    - Single character strings (returns a tuple with one element).
    - Strings with spaces, numbers, and special characters.

    Args:
        input_str: The string to be converted. Must be a non-null string.

    Returns:
        A tuple where each element is a single character from the input string.

    Raises:
        TypeError: If the input is not a string or is None.
    """
    # Step 1: Validate the input explicitly.
    validated_input = _validate_input(input_str, "string")

    # Step 2: Process the validated string to extract individual characters.
    # This loop explicitly iterates to build the list, avoiding dense comprehensions
    # to satisfy the requirement for explicit control flow and intermediate variables.
    char_list = _convert_string_to_characters(validated_input)

    # Step 3: Convert the list of characters into the final tuple structure.
    result_tuple = _convert_list_to_tuple(char_list)

    return result_tuple