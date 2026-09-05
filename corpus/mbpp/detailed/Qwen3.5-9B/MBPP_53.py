from typing import Union, Tuple, Optional

# Define specific error classes for more informative exception handling
class InvalidInputTypeError(TypeError):
    """Raised when the input type is not a string."""
    pass

class EmptyInputError(ValueError):
    """Raised when the input string has zero length."""
    pass

def _validate_input(input_value: object) -> str:
    """
    Validates that the input is a non-empty string.

    Args:
        input_value: The value to validate.

    Returns:
        The validated string.

    Raises:
        InvalidInputTypeError: If input is not a string.
        EmptyInputError: If input is an empty string.
    """
    # Check type explicitly
    if not isinstance(input_value, str):
        raise InvalidInputTypeError(
            f"Input must be of type 'str', but received type '{type(input_value).__name__}'."
        )

    # Check for empty string explicitly
    if len(input_value) == 0:
        raise EmptyInputError("Input string cannot be empty.")

    return input_value

def _extract_boundary_characters(validated_string: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Extracts the first and last characters from the validated string.

    This function handles the case where the string has exactly one character,
    ensuring both returned characters exist for comparison logic.

    Args:
        validated_string: A non-empty string.

    Returns:
        A tuple containing (first_char, last_char).
    """
    string_length = len(validated_string)

    # Determine the index of the first character
    first_index = 0

    # Determine the index of the last character
    last_index = string_length - 1

    # Fetch characters using safe indexing
    first_char = validated_string[first_index]
    last_char = validated_string[last_index]

    return first_char, last_char

def _compare_characters(first_char: str, last_char: str) -> str:
    """
    Compares two characters and returns a status string.

    Args:
        first_char: The first character.
        last_char: The last character.

    Returns:
        "Equal" if characters match, "Not Equal" otherwise.
    """
    if first_char == last_char:
        return "Equal"
    else:
        return "Not Equal"

def check_Equality(input_string: str) -> str:
    """
    Checks whether the first and last characters of a given string are equal.

    This function performs rigorous validation and explicit step-by-step logic
    to determine if the boundary characters match. It handles edge cases such as:
    - Non-string inputs (raises error)
    - Empty strings (raises error)
    - Single-character strings (considers first and last as the same character)
    - Strings with differing first and last characters

    Args:
        input_string: The string to analyze.

    Returns:
        "Equal" if the first and last characters are identical.
        "Not Equal" if the first and last characters are different.

    Raises:
        InvalidInputTypeError: If input_string is not a string.
        EmptyInputError: If input_string is empty.

    Examples:
        >>> check_Equality("abcda")
        'Equal'
        >>> check_Equality("ab")
        'Not Equal'
        >>> check_Equality("mad")
        'Not Equal'
        >>> check_Equality("a")
        'Equal'
        >>> check_Equality("aaaa")
        'Equal'
    """
    # Step 1: Validate the input immediately
    validated_input = _validate_input(input_string)

    # Step 2: Extract the specific characters needed for comparison
    first_char, last_char = _extract_boundary_characters(validated_input)

    # Step 3: Perform the comparison and return the result
    return _compare_characters(first_char, last_char)