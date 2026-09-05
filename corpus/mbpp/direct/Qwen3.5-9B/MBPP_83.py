def get_Char(s):
    result = 0
    for char in s:
        result += ord(char)
    return chr(result)