def remove_lowercase(s):
    result = []
    for char in s:
        if not char.islower():
            result.append(char)
    return ''.join(result)