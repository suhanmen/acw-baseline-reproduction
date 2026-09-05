def minimum_Length(s):
    min_len = len(s)
    for c in set(s):
        new_s = s.replace(c, '')
        if len(new_s) < min_len:
            min_len = len(new_s)
    return min_len