import re

def check_literals(text: str, literals: list) -> str:
    """
    Searches for a list of literal strings in a given text using regex.
    Returns 'Matched!' if at least one literal is found, otherwise 'Not Matched!'.
    """
    for literal in literals:
        # re.escape is used to ensure literal strings are treated as literals 
        # even if they contain regex special characters.
        if re.search(re.escape(literal), text):
            return 'Matched!'
    return 'Not Matched!'