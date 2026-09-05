import re
from typing import List

def is_alphanumeric_char(char: str) -> bool:
    """
    Determines if a single character is alphanumeric.

    Args:
        char: A single character string.

    Returns:
        bool: True if the character is a letter or a digit, False otherwise.
    """
    # We check if the character is a letter or a digit.
    # This excludes spaces, punctuation, and special symbols.
    return char.isalnum()

def remove_splchar(input_string: str) -> str:
    """
    Removes all characters from a string except for alphanumeric characters.
    Spaces, punctuation, and special symbols are discarded.

    Args:
        input_string: The string to process.

    Returns:
        str: A new string containing only alphanumeric characters.

    Raises:
        TypeError: If the input is not a string.
    """
    # Defensive Check: Ensure the input is a string.
    if not isinstance(input_string, str):
        raise TypeError(f"Input must be a string, but received {type(input_string).__name__}")

    # Handle edge case: Empty string.
    if not input_string:
        return ""

    # Initialize a list to collect valid characters.
    # Using a list for construction is more efficient than repeated string concatenation.
    filtered_chars: List[str] = []

    # Iterate through every character in the input string.
    for char in input_string:
        # Validate if the character is alphanumeric.
        if is_alphanumeric_char(char):
            # If valid, append to our collection.
            filtered_chars.append(char)

    # Join the list of characters back into a single string.
    result_string = "".join(filtered_chars)

    return result_string

if __name__ == "__main__":
    # Test cases provided in the prompt requirements.
    assert remove_splchar('python  @#&^%$*program123') == 'pythonprogram123'
    assert remove_splchar('python %^$@!^&*()  programming24%$^^()    language') == 'pythonprogramming24language'
    assert remove_splchar('python   ^%&^()(+_)(_^&67)                  program') == 'python67program'

    # Additional Edge Cases:
    # Empty String
    assert remove_splchar('') == ''
    # All Special Characters
    assert remove_splchar('!@#$%^&*()_+=-[]{}|;:\",.<>?/`~ ') == ''
    # All Alphanumeric (No changes)
    assert remove_splchar('Python310') == 'Python310'
    # Single Alphanumeric
    assert remove_splchar('a') == 'a'
    # Single Special
    assert remove_splchar('!') == ''
    # Numbers only
    assert remove_splchar('123 456') == '123456'