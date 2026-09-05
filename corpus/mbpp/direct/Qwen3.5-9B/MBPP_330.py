import re

def find_char(s: str) -> list:
    words = re.findall(r"\b[A-Za-z]{3,5}\b", s)
    return words