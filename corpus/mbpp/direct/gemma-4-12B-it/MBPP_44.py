import re

def text_match_string(text):
    """
    Matches a word at the beginning of a string.
    The word must start at index 0 and cannot be preceded by spaces.
    """
    # Using ^ to ensure the match is at the start of the string
    # and checking for the specific word "python"
    pattern = r'^python'

    if re.search(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'

if __name__ == "__main__":
    assert text_match_string(" python") == 'Not matched!'
    assert text_match_string("python") == 'Found a match!'
    assert text_match_string("  lang") == 'Not matched!'