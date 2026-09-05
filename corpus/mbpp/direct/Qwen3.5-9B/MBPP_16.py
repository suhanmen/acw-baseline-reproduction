import re

def text_lowercase_underscore(text):
    pattern = re.compile(r'[a-z]+_[a-z]+')
    if pattern.search(text):
        return 'Found a match!'
    return 'Not matched!'