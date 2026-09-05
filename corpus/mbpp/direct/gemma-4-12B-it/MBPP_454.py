import re

def text_match_wordz(text):
    """
    Matches a word containing the letter 'z'.
    Returns 'Found a match!' if a word with 'z' exists, otherwise 'Not matched!'.
    """
    # The pattern \b\w*z\w*\b checks for a word boundary, 
    # then any word characters, then 'z', then any word characters, 
    # then a word boundary.
    patterns = r'\b\w*z\w*\b'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return 'Not matched!'