def remove_lowercase(s: str) -> str:
    """
    Removes all lowercase substrings from a given string, 
    returning only the uppercase characters.
    """
    return "".join(char for char in s if char.isupper())

if __name__ == "__main__":
    assert remove_lowercase("PYTHon") == 'PYTH'
    assert remove_lowercase("FInD") == 'FID'
    assert remove_lowercase("STRinG") == 'STRG'