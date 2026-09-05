from typing import List


def text_match_string(input_string: str) -> str:
    """
    Checks if the string starts exactly with the word "python".

    Args:
        input_string (str): The string to be checked.

    Returns:
        str: 'Found a match!' if the string starts with "python", 
             otherwise 'Not matched!'.
    """
    # Define the target word to match
    target_word: str = "python"

    # 1. Validation: Ensure the input is a string.
    # While the prompt implies string input, production code should handle 
    # unexpected types gracefully.
    if not isinstance(input_string, str):
        # In a real production system, we might raise a TypeError.
        # Here, we treat non-strings as non-matches.
        return "Not matched!"

    # 2. Handle edge cases: Empty string.
    if len(input_string) == 0:
        return "Not matched!"

    # 3. Check for a match at the very beginning.
    # The requirement is to match the word at the beginning.
    # Leading whitespace should result in a non-match based on the provided 
    # test cases ("  lang" -> 'Not matched!').

    # We use .startswith() to ensure it is at the beginning of the string.
    # We do NOT strip the input string, because leading spaces would invalidate
    # the "at the beginning" requirement for the word "python".

    is_match: bool = input_string.startswith(target_word)

    # 4. Determine the result message based on the match.
    if is_match:
        result_message: str = "Found a match!"
    else:
        result_message: str = "Not matched!"

    return result_message

# Assertions provided in the problem
if __name__ == "__main__":
    # Test Case 1: Leading space should fail
    assert text_match_string(" python") == 'Not matched!'

    # Test Case 2: Exact start match should succeed
    assert text_match_string("python") == 'Found a match!'

    # Test Case 3: Leading space with different word should fail
    assert text_match_string("  lang") == 'Not matched!'

    # Additional Defensive Test Cases:
    # Empty string
    assert text_match_string("") == 'Not matched!'
    # String containing "python" but not at the start
    assert text_match_string("I love python") == 'Not matched!'
    # String that is "python" followed by other text
    assert text_match_string("pythonic_code") == 'Found a match!'
    # Case sensitivity check (assuming strict match)
    assert text_match_string("Python") == 'Not matched!'