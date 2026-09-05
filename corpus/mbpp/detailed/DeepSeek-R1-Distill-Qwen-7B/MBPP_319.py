import re

def find_long_word(s):
    """
    Finds all five-character long words in the given string using regex.

    Args:
        s (str): The input string to search for words.

    Returns:
        list: A list of five-character words found in the string.
    """
    if not isinstance(s, str):
        return []

    # Find all words of exactly five letters
    matches = re.findall(r'\b[a-zA-Z]{5}\b', s)

    # Convert to lowercase
    matches_lower = [match.lower() for match in matches]

    # Filter out matches that are not exactly five letters
    valid_matches = [m for m in matches_lower if len(m) == 5]

    return valid_matches