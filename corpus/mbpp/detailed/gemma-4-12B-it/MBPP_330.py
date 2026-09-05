import re
from typing import List

def find_char(input_string: str) -> List[str]:
    """
    Finds all words in the given string that have a length of 3, 4, or 5 characters.

    The function uses regular expressions to identify word boundaries and extract
    words. It validates the input to ensure it is a string and handles 
    various edge cases like empty strings or strings with only special characters.

    Args:
        input_string (str): The string to search for words.

    Returns:
        List[str]: A list of words with lengths 3, 4, or 5.
    """
    # Input Validation: Check if the input is a string
    if not isinstance(input_string, str):
        raise ValueError(f"Input must be a string, received {type(input_string).__name__}")

    # Handle edge case: Empty input string
    if not input_string.strip():
        return []

    # Define the regular expression pattern.
    # \b is a word boundary.
    # \w matches any alphanumeric character (equivalent to [a-zA-Z0-9_]).
    # {3,5} ensures the length is between 3 and 5 inclusive.
    # We use capturing groups to isolate the words.
    word_pattern = re.compile(r'\b\w{3,5}\b')

    # Extract all matches using findall
    # findall returns a list of strings matching the pattern
    raw_matches = word_pattern.findall(input_string)

    # Filter the matches to ensure they are strictly 3, 4, or 5 characters long.
    # While the regex \w{3,5} covers this, we explicitly check for clarity 
    # and to handle any nuances in word boundary behavior.
    valid_words = []
    for word in raw_matches:
        word_length = len(word)
        if 3 <= word_length <= 5:
            valid_words.append(word)

    return valid_words

# Standard assertions for verification
if __name__ == "__main__":
    # Test Case 1
    result1 = find_char('For the four consumer complaints contact manager AKR reddy')
    assert result1 == ['For', 'the', 'four', 'AKR', 'reddy']

    # Test Case 2
    result2 = find_char('Certain service are subject to change MSR')
    assert result2 == ['are', 'MSR']

    # Test Case 3
    result3 = find_char('Third party legal desclaimers')
    assert result3 == ['Third', 'party', 'legal']