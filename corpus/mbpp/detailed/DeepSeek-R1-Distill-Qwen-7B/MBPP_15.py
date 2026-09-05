def split_lowerstring(s):
    if not isinstance(s, str):
        return None

    result = []
    current = []

    for char in s:
        if char.islower():
            if current:
                result.append(''.join(current))
                current = []
            current.append(char)
        else:
            current.append(char)

    if current:
        result.append(''.join(current))

    return result