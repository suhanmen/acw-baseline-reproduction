def common_prefix(strings, limit):
    if not strings:
        return ""
    prefix = strings[0][:limit]
    for s in strings[1:]:
        if not s[:limit].startswith(prefix):
            return ""
    # Check the actual common prefix within the limit
    for i in range(limit):
        chars = set(s[i] for s in strings if i < len(s))
        if len(chars) != 1:
            return prefix[:i]
    return prefix[:limit]