import re

def text_match_wordz(text: str) -> str:
    pattern = r'\bz\w*\b'
    if re.search(pattern, text, re.IGNORECASE):
        return "Found a match!"
    return "Not matched!"