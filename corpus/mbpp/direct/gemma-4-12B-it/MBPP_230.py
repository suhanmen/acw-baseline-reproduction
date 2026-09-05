def replace_blank(text: str, char: str) -> str:
    """
    Replaces all blank spaces in a string with a given character.
    """
    return text.replace(" ", char)

if __name__ == "__main__":
    assert replace_blank("hello people", '@') == "hello@people"
    assert replace_blank("python program language", '$') == "python$program$language"
    assert replace_blank("blank space", "-") == "blank-space"