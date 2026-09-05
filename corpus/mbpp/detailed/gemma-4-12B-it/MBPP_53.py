def check_Equality(input_string: str) -> str:
    """
    Checks whether the first and last characters of a given string are equal.

    Args:
        input_string (str): The string to be evaluated.

    Returns:
        str: "Equal" if the first and last characters match, 
             "Not Equal" otherwise.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input string is empty.
    """

    # --- Input Validation ---

    # Check if the input is actually a string type
    if not isinstance(input_string, str):
        raise TypeError(f"Expected input type 'str', but received '{type(input_string).__name__}'")

    # Check for empty string (edge case: cannot have first/last chars if empty)
    if len(input_string) == 0:
        raise ValueError("Input string cannot be empty.")

    # --- Logic Implementation ---

    # Extract the first character
    # Using indexing directly as we've already validated that the length is at least 1
    first_char = input_string[0]

    # Extract the last character
    # Using negative indexing to retrieve the character at the end
    last_char = input_string[-1]

    # Comparison Logic
    # We perform a direct equality check
    is_match = (first_char == last_char)

    # Determine the return string based on the result of the comparison
    if is_match:
        result = "Equal"
    else:
        result = "Not Equal"

    return result

# Assertions provided in the problem description
if __name__ == "__main__":
    # These check that the function adheres to the requirements.
    assert check_Equality("abcda") == "Equal"
    assert check_Equality("ab") == "Not Equal"
    assert check_Equality("mad") == "Not Equal"

    # Additional implicit edge cases handled by logic:
    # Single character string: "a" -> First and Last are both 'a' -> "Equal"
    assert check_Equality("a") == "Equal"
    # Case sensitivity: "A" vs "a" -> "Not Equal"
    assert check_Equality("AbA") == "Equal"
    assert check_Equality("Aba") == "Not Equal"