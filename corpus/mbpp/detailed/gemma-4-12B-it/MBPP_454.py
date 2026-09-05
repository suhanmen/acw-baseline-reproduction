from typing import List

def text_match_wordz(text: str) -> str:
    """
    Checks if a given string contains the character 'z'.

    Args:
        text (str): The input string to search for the character 'z'.

    Returns:
        str: 'Found a match!' if 'z' is present, otherwise 'Not matched!'.

    Raises:
        TypeError: If the input is not a string.
    """
    # Input Validation
    if not isinstance(text, str):
        raise TypeError(f"Input must be a string, but received {type(text).__name__}")

    # Handle degenerate case: Empty string
    if len(text) == 0:
        return "Not matched!"

    # The logic is to check if the character 'z' exists anywhere in the string.
    # We iterate through each character to ensure clear, explicit logic.
    is_match_found: bool = False

    for character in text:
        # Using lowercase 'z' as specified by the logic of the problem requirements
        if character == 'z':
            is_match_found = True
            # Once we find one 'z', we can stop searching
            break

    # Determine the result based on the search outcome
    if is_match_found:
        result_message = "Found a match!"
    else:
        result_message = "Not matched!"

    return result_message

if __name__ == "__main__":
    # The assertions provided in the problem description
    assert text_match_wordz("pythonz.") == 'Found a match!'
    assert text_match_wordz("xyz.") == 'Found a match!'
    assert text_match_wordz("  lang  .") == 'Not matched!'