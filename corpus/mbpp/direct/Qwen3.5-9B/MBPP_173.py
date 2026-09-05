import re

def remove_splchar(s: str) -> str:
    return re.sub(r'[^a-zA-Z0-9]', '', s)