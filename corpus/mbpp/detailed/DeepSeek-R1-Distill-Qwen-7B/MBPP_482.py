import re

def match(string):
    # Check if the string is empty
    if not string:
        return 'No'

    # Check if the string has at least one character
    if len(string) < 2:
        return 'No'

    # Check if all characters are letters (a-z or A-Z)
    if not re.match('^[a-zA-Z]+$', string):
        return 'No'

    # Compile the regex pattern
    pattern = re.compile(r'^([A-Z][a-z]+)$')

    # Search for the pattern in the string
    if pattern.search(string):
        return 'Yes'
    else:
        return 'No'