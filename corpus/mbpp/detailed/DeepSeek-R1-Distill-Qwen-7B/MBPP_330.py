import re

def find_char(string):
    """
    Find all words in the given string that are 3, 4, or 5 characters long using regex.

    Args:
        string (str): The input string to search.

    Returns:
        list: A list of words that are 3, 4, or 5 characters long.
    """
    if not string:
        return []

    # Define the regex pattern to match words of length 3-5
    pattern = r'\b\w{3,5}\b'

    # Find all matches in the string
    matches = re.findall(pattern, string)

    # Filter the matches to include only words of length 3,4,5
    result = [word for word in matches if len(word) in {3,4,5}]

    # Return the result
    return result