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
    # Handle empty string case
    if not txt:
        return False

    # Remove leading and trailing whitespace
    trimmed_txt = txt.strip()

    # Check if the string is empty after trimming
    if not trimmed_txt:
        return False

    # Split the text into words
    words = trimmed_txt.split()

    # If there's only one word, check if it's a single character
    if len(words) == 1:
        return len(trimmed_txt) != 1

    # Check the last word's length
    last_word = words[-1]
    if len(last_word) == 1:
        return False

    # Check the last character of the entire string
    last_char = trimmed_txt[-1]
    if not last_char.isalpha():
        return False

    # Check that the previous character is different
    if trimmed_txt[-2] == trimmed_txt[-1]:
        return False

    # All conditions met
    return True