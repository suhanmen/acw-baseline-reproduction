import re

def match(s):
    pattern = re.compile(r'[A-Z][a-z]*')
    if pattern.search(s):
        return 'Yes'
    return 'No'