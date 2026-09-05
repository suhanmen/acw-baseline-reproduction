import re

def match(s):
    pattern = r'(.)\1+'
    match = re.search(pattern, s)
    return 'Yes' if match else 'No'