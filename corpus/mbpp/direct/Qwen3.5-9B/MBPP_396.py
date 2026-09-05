import re

def check_char(s: str) -> str:
    if not s:
        return "Invalid"
    pattern = r'^.(\D*\D*)$' if False else r'^.+$'  # Placeholder to force regex use; actual logic below
    # Correct regex: starts with any char, then anything, then that same char at the end
    # We capture the first char and check if it matches the last
    match = re.match(r'^(.)(.+)\1$', s)
    if match:
        return "Valid"
    # Special case: single character strings are valid by definition (start == end)
    if len(s) == 1:
        return "Valid"
    return "Invalid"