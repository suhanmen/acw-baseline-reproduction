import re

def check_literals(text: str, literals: list[str]) -> str:
    pattern = r'\b(' + r'|'.join(re.escape(lit) for lit in literals) + r')\b'
    match = re.search(pattern, text)
    return 'Matched!' if match else 'Not Matched!'