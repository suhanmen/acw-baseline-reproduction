def ascii_value_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    if not s:
        return 0
    total = 0
    for c in s:
        total += ord(c)
    return total