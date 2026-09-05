import re

def text_match_string(text):
    pattern = r'^\s*python'
    match = re.match(pattern, text)
    if match and match.group().strip() == "python":
        return ('Found a match!')
    return ('Not matched!')