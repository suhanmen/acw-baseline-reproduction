def remove_Char(s: str, char: str) -> str:
    return char.join(c for c in s if c != char)