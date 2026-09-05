def remove_Char(input_string: str, char_to_remove: str) -> str:
    """
    Removes all occurrences of a specified character from a given string.
    """
    return input_string.replace(char_to_remove, "")

if __name__ == "__main__":
    assert remove_Char("aba", 'a') == "b"
    assert remove_Char("toggle", 'g') == "tole"
    assert remove_Char("aabbc", 'b') == "aac"