def ascii_value(char):
    if not isinstance(char, str) or len(char) != 1:
        raise ValueError("Input must be a single character string.")
    if not char.isalpha():
        raise ValueError("Input must be an alphabetic character.")
    return ord(char)