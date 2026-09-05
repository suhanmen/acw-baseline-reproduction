import re
from typing import List

def check_literals(input_string: str, literals: List[str]) -> str:
    """
    Searches for a list of literal strings within a source string using regex.
    If any of the literals are found, returns 'Matched!'.
    Otherwise, returns 'Not Matched!'.

    Args:
        input_string (str): The main text to search within.
        literals (List[str]): A list of strings to search for.

    Returns:
        str: 'Matched!' if at least one literal is found, 'Not Matched!' otherwise.

    Raises:
        TypeError: If input_string is not a string or literals is not a list.
        ValueError: If any literal contains characters that are invalid for regex.
    """

    # --- Input Validation ---

    if not isinstance(input_string, str):
        raise TypeError(f"Expected input_string to be str, got {type(input_string).__name__}")

    if not isinstance(literals, list):
        raise TypeError(f"Expected literals to be a list, got {type(literals).__name__}")

    # Check if all elements in the literals list are strings
    for index, item in enumerate(literals):
        if not isinstance(item, str):
            raise TypeError(f"Element at index {index} in literals list must be a string.")

    # --- Edge Case Handling ---

    # If the list of literals is empty, it cannot match anything.
    if not literals:
        return "Not Matched!"

    # If the input string is empty, it can only match if one of the literals is an empty string.
    # However, regex behavior for empty strings can be tricky; we handle it explicitly.
    if input_string == "":
        for literal in literals:
            if literal == "":
                return "Matched!"
        return "Not Matched!"

    # --- Matching Logic ---

    # We iterate through each literal provided in the list.
    for literal in literals:
        # If the literal is an empty string, it is technically "found" at the start of any string.
        if literal == "":
            return "Matched!"

        try:
            # We use re.escape to ensure that special regex characters (like '.', '*', '+', etc.)
            # inside the literal strings are treated as literal characters rather than regex operators.
            escaped_literal = re.escape(literal)

            # Create a regex pattern object.
            # We do not use re.IGNORECASE as the prompt implies literal matching.
            pattern = re.compile(escaped_literal)

            # Attempt to find the pattern in the input string.
            match_object = pattern.search(input_string)

            # If a match object is returned (not None), we have found at least one literal.
            if match_object is not None:
                return "Matched!"

        except re.error as e:
            # This block handles cases where regex compilation might fail despite re.escape.
            # In production, you might want to log this error.
            raise ValueError(f"Regex compilation failed for literal '{literal}': {e}")

    # If the loop completes without returning, no literals were found.
    return "Not Matched!"