import re

def text_match(s):
    pattern = r"(\w+)_\w+"
    return 'Found a match!' if re.search(pattern, s, flags=re.IGNORECASE) else 'Not matched!'