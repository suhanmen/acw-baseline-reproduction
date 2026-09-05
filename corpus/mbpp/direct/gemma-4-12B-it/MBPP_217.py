def first_Repeated_Char(s: str) -> str:
    """
    Finds the first character in a string that appears more than once.
    If no character is repeated, returns '\0'.
    """
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return '\0'