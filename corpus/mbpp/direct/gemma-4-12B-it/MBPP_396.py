import re

def check_char(s: str) -> str:
    """
    Checks whether the given string starts and ends with the same character 
    using a regular expression.
    """
    if not s:
        return "Invalid"

    # Regex explanation:
    # ^(.) matches the first character and captures it in group 1
    # .* matches any characters in between
    # \1$ matches the same character captured in group 1 at the end of the string
    # For a single character string, ^(.) matches the start and end simultaneously
    pattern = r'^(.).*\1$'

    # Special case for single character strings as they technically start and end with the same char
    if len(s) == 1:
        return "Valid"

    if re.match(pattern, s):
        return "Valid"
    else:
        return "Invalid"