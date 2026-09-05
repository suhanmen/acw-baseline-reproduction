def remove_lowercase(s):
    result = []
    for c in s:
        if c.islower():
            continue
        result.append(c)
    return ''.join(result)