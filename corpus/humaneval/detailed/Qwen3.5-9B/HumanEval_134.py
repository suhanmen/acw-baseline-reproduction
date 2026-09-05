import re
import string


def _is_valid_string(input_value):
    """
    Validates that the input is a string.
    Raises a TypeError if the input is not a string.

    :param input_value: The value to validate.
    :raises TypeError: If the input is not an instance of str.
    :return: The validated string.
    """
    if not isinstance(input_value, str):
        raise TypeError(f"Expected input to be a string, but got {type(input_value).__name__}")
    return input_value


def _is_alphabetic_character(char):
    """
    Checks if a single character is an alphabetical letter (A-Z or a-z).

    :param char: A single character to check.
    :return: True if the character is an alphabetical letter, False otherwise.
    """
    return char in string.ascii_letters


def _strip_trailing_whitespace(txt):
    """
    Removes trailing whitespace characters from the end of a string.

    :param txt: The input string.
    :return: The string with trailing whitespace removed.
    """
    return txt.rstrip()


def _get_last_character(txt):
    """
    Safely retrieves the last character of a non-empty string.
    Returns None if the string is empty.

    :param txt: The input string.
    :return: The last character or None if the string is empty.
    """
    if len(txt) == 0:
        return None
    return txt[-1]


def _is_last_char_isolated(txt):
    """
    Determines if the last character is a word boundary.
    A last character is considered isolated if:
    1. It is an alphabetical character.
    2. The character immediately preceding it (if it exists) is NOT an alphabetical character.
       This includes cases where the preceding character is a space or the string starts with the character.

    Note: We do not check the right side because it is the end of the string.

    :param txt: The input string.
    :return: True if the last character is an isolated letter, False otherwise.
    """
    if len(txt) == 0:
        return False

    last_char = txt[-1]

    # Condition 1: The last character must be an alphabetical letter
    if not _is_alphabetic_character(last_char):
        return False

    # Check the character before the last one
    # If the string has only one character, it is considered isolated 
    # because there is no preceding character to form a "word".
    if len(txt) == 1:
        return True

    prev_char = txt[-2]

    # Condition 2: The preceding character must not be an alphabetical letter.
    # If the preceding character is a letter, then the last character is part of a word.
    # If the preceding character is a space or any other non-letter, it is a boundary.
    if _is_alphabetic_character(prev_char):
        return False

    # If we are here, the last char is a letter and the one before is not.
    return True


def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    """

    # Step 1: Validate input type
    try:
        validated_txt = _is_valid_string(txt)
    except TypeError as e:
        # In a production setting, we might want to re-raise or handle differently.
        # Here we strictly follow the requirement to deal with invalid inputs.
        raise e

    # Step 2: Handle empty string case explicitly
    if validated_txt == "":
        return False

    # Step 3: Retrieve the last character
    last_char = _get_last_character(validated_txt)

    # Step 4: Check if the last character is an alphabetical letter
    is_letter = _is_alphabetic_character(last_char)

    if not is_letter:
        return False

    # Step 5: Determine if the letter is isolated (not part of a word)
    # The definition of "not part of a word" implies it is separated from other letters 
    # on its left side (since there is nothing on the right).
    is_isolated = _is_last_char_isolated(validated_txt)

    return is_isolated