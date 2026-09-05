def unique_Characters(s: str) -> bool:
    """
    Checks whether all the characters in a given string are unique.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if all characters are unique, False otherwise.
    """
    return len(set(s)) == len(s)

if __name__ == "__main__":
    assert unique_Characters('aba') == False
    assert unique_Characters('abc') == True
    assert unique_Characters('abab') == False