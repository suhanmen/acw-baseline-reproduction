def check_String(s):
    has_letter = False
    has_number = False
    for char in s:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_number = True
    return has_letter and has_number