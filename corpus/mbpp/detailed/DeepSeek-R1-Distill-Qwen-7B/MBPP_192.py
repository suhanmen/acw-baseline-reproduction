def check_String(s):
    def is_letter(c):
        return c.isalpha()

    def is_number(c):
        return c.isdigit()

    if not isinstance(s, str):
        return False

    has_letter = False
    has_number = False

    for char in s:
        if is_letter(char):
            has_letter = True
        elif is_number(char):
            has_number = True

    return has_letter and has_number