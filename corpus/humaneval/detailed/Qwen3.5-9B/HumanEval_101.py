import re
from typing import List, Union

def words_string(s: Union[str, None]) -> List[str]:
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.

    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]

    This function explicitly handles:
    - None input
    - Empty string input
    - Strings with only whitespace or separators
    - Mixed separators (commas and spaces)
    - Leading/trailing whitespace or separators
    - Multiple consecutive separators

    The function validates that the input is a string (not an integer, float, list, etc.)
    and raises a TypeError if the input type is invalid.

    Args:
        s: The input string to be split into words.

    Returns:
        A list of strings representing the individual words from the input.

    Raises:
        TypeError: If the input is not a string.
    """

    # Step 1: Validate the input type explicitly
    if s is None:
        raise TypeError("Input must be a string, received None.")

    # Check if the input is a string
    if not isinstance(s, str):
        raise TypeError(f"Input must be a string, received {type(s).__name__}.")

    # Step 2: Handle the empty string case explicitly
    if len(s) == 0:
        return []

    # Step 3: Normalize the input string by stripping leading and trailing whitespace
    # This is important for cases where the string starts or ends with whitespace
    normalized_string = s.strip()

    # Step 4: Handle the case where the string contains only whitespace after stripping
    # In this case, there are no actual words to extract
    if len(normalized_string) == 0:
        return []

    # Step 5: Define a regex pattern that matches one or more non-whitespace, non-comma characters
    # This pattern will capture individual words, treating commas and spaces as delimiters
    # The pattern [^,\s]+ matches one or more characters that are NOT a comma or whitespace
    word_pattern = r'[^,\s]+'

    # Step 6: Use the re.findall function to extract all matching words from the normalized string
    # This handles both commas and spaces as separators automatically
    raw_words = re.findall(word_pattern, normalized_string)

    # Step 7: Filter out any empty strings that might have been captured (defensive programming)
    # Although the regex pattern should not produce empty matches, this adds an extra layer of safety
    cleaned_words = [word for word in raw_words if len(word) > 0]

    # Step 8: Return the final list of words
    return cleaned_words