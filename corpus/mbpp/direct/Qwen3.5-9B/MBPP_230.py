def replace_blank(s, char):
    result = []
    for i, c in enumerate(s):
        if c == ' ':
            result.append(char)
        else:
            result.append(c)
    return ''.join(result)