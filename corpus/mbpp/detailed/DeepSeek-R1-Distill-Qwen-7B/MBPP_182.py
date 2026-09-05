def find_character(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")

    uppercase = []
    lowercase = []
    special_char = []
    numeric = []

    for char in s:
        if 'A' <= char <= 'Z':
            uppercase.append(char)
        elif 'a' <= char <= 'z':
            lowercase.append(char)
        elif '0' <= char <= '9':
            numeric.append(char)
        else:
            special_char.append(char)

    return (uppercase, lowercase, special_char, numeric)