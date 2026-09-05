def remove_dirty_chars(s1, s2):
    s1_list = list(s1)
    s2_set = set(s2)
    result = []
    for char in s1_list:
        if char not in s2_set:
            result.append(char)
    return ''.join(result)