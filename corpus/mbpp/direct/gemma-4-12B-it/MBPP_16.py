import re

def text_lowercase_underscore(text):
    """
    Finds sequences of lowercase letters joined with an underscore.
    The regex checks if the entire string consists only of lowercase letters 
    separated by an underscore, with no leading/trailing characters 
    other than the lowercase letters.
    """
    # Match start of string, one or more lowercase letters, 
    # an underscore, then one or more lowercase letters, end of string.
    pattern = r'^[a-z]+_[a-z]+$'

    if re.match(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'