import re

def text_match_word(text: str) -> str:
    pattern = r'\b\w+$'
    if re.search(pattern, text.rstrip()):
        return 'Found a match!'
    return 'Not matched!'