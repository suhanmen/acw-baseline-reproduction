import re

def find_long_word(text: str) -> list:
    pattern = r'\b[a-zA-Z]{5}\b'
    return re.findall(pattern, text)