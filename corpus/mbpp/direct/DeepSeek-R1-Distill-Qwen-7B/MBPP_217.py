def first-Repeated_Char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            return char
        char_count[char] = 1
    return '\0'