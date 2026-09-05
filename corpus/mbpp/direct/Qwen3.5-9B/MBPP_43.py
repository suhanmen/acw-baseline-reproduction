import re

def text_match(text):
    pattern = r'^[a-z]+(_[a-z]+)*$'
    if re.match(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'