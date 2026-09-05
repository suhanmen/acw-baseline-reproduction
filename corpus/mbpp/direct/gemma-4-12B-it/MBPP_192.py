def check_String(s: str) -> bool:
    """
    Checks whether a string has at least one letter and one number.
    """
    has_letter = False
    has_number = False

    for char in s:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_number = True

        if has_letter and has_number:
            return True

    return False

if __name__ == "__main__":
    assert check_String('thishasboth29') == True
    assert check_String('python') == False
    assert check_String('string') == False