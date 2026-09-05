import re

def remove_whitespaces(s: str) -> str:
    return re.sub(r'\s', '', s)