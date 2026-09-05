import re

def text_match_one(text):
    if re.fullmatch(r'a+b', text):
        return 'Found a match!'
    return 'Not matched!'