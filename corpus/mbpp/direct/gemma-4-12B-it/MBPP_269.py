def ascii_value(char: str) -> int:
    """
    Returns the ASCII value of a given character.

    Args:
        char (str): A single character string.

    Returns:
        int: The ASCII integer value of the character.
    """
    return ord(char)

if __name__ == "__main__":
    assert ascii_value('A') == 65
    assert ascii_value('R') == 82
    assert ascii_value('S') == 83