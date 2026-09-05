import re

def _is_valid_string(text):
    """
    Validates that the input is indeed a string type.

    Returns True if valid, raises TypeError otherwise.
    """
    if not isinstance(text, str):
        raise TypeError(f"Input must be a string, got {type(text).__name__}")
    return True

def _extract_match_result(text: str) -> str:
    """
    Core logic to check if a word exists at the beginning of the string.

    Steps:
    1. Strip leading whitespace to check content start.
    2. Compare the stripped version of the text with the original start.
    3. Return appropriate message.

    This function does not use regex directly to ensure explicit step-by-step logic.
    However, given the requirement to match a "word" at the beginning, 
    we interpret this as checking if the text starts with a non-whitespace word.

    Based on the assertions:
    - " python" -> 'Not matched!' (starts with space)
    - "python" -> 'Found a match!' (starts immediately with word)
    - "  lang" -> 'Not matched!' (starts with spaces)

    Therefore, the condition is: text[0] must not be a whitespace character.
    """
    _validate_input(text)

    # Check if string is empty
    if len(text) == 0:
        return 'Not matched!'

    # Check if the first character is a whitespace
    first_char = text[0]
    is_whitespace = first_char.isspace()

    if is_whitespace:
        return 'Not matched!'
    else:
        return 'Found a match!'

def _validate_input(text: str):
    """
    Wrapper to ensure input validation happens at the right place.
    """
    _is_valid_string(text)

def text_match_string(text: str) -> str:
    """
    Matches a word at the beginning of a string.

    Returns:
        'Found a match!' if a word starts the string (ignoring leading whitespace logic based on test cases)
        'Not matched!' otherwise.

    Based on the provided assertions:
    - " python" fails because it starts with a space.
    - "python" passes because it starts with 'p'.
    - "  lang" fails because it starts with a space.

    The logic implies that any leading whitespace causes a mismatch.
    """
    result = _extract_match_result(text)
    return result

# Re-exporting the main function as required by the problem statement signature
# The function name is 'text_match_string' and takes one argument 'text'.