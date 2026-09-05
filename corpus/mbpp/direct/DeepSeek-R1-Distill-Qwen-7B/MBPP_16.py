import re

def text_lowercase_underscore(s):
    pattern = r'.*_[a-z]+_[a-z]+$'
    if re.fullmatch(pattern, s):
        return 'Found a match!'
    else:
        return 'Not matched!'