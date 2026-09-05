def split_lowerstring(s):
    result = []
    start = 0
    for i, c in enumerate(s):
        if c.islower():
            result.append(s[start:i])
            start = i
    # Add the last substring
    if start < len(s):
        result.append(s[start:])
    return result