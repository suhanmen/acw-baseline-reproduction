import re

def text_match_one(text: str) -> str:
    """
    Matches a string that contains an 'a' followed by one or more 'b's.

    Args:
        text (str): The input string to be checked.

    Returns:
        str: 'Found a match!' if the pattern exists, otherwise 'Not matched!'.

    Raises:
        TypeError: If the input is not a string.
    """
    # Validate input type
    if not isinstance(text, str):
        raise TypeError(f"Input must be a string, received {type(text).__name__}")

    # Handle empty string edge case explicitly
    if len(text) == 0:
        return "Not matched!"

    # Define the pattern:
    # 'a' followed by 'b' repeated one or more times
    # We use a regex pattern for clarity and correctness.
    # 'a' matches the literal character 'a'
    # 'b+' matches the character 'b' one or more times
    pattern = r"ab+"

    try:
        # Search the string for the pattern
        # re.search finds the first location where the pattern produces a match
        match_result = re.search(pattern, text)

        # Evaluate the match result
        if match_result is not None:
            return "Found a match!"
        else:
            return "Not matched!"

    except Exception as e:
        # General catch for unexpected errors during regex processing
        # In a production environment, this might be logged.
        return "Not matched!"

# The following assertions ensure the function behaves as required.
if __name__ == "__main__":
    # These are the required assertions provided in the problem description
    assert text_match_one("ac") == 'Not matched!'
    assert text_match_one("dc") == 'Not matched!'
    assert text_match_one("abba") == 'Found a match!'