import re

def remove_uppercase(s: str) -> str:
    return re.sub(r'[A-Z]+', '', s)