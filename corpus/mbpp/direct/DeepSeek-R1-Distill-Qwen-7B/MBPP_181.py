def common_prefix(strings, length):
    if not strings:
        return ""
    for i in range(length):
        current_char = strings[0][i]
        for string in strings[1:]:
            if i >= len(string) or string[i] != current_char:
                return strings[0][:i]
    return strings[0][:length]