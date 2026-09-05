def get_Char(s):
    total = 0
    for char in s:
        total += ord(char)
    return chr(total)