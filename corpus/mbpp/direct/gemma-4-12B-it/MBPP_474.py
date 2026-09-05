def replace_char(input_str: str, old_char: str, new_char: str) -> str:
    """
    Replaces all occurrences of old_char in input_str with new_char.
    """
    return input_str.replace(old_char, new_char)

# Test cases
if __name__ == "__main__":
    assert replace_char("polygon", 'y', 'l') == "pollgon"
    assert replace_char("character", 'c', 'a') == "aharaater"
    assert replace_char("python", 'l', 'a') == "python"