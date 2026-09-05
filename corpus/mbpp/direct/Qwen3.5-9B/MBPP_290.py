def max_length(lst):
    if not lst:
        return (0, [])
    max_len = -1
    result = []
    for item in lst:
        length = len(item)
        if length > max_len:
            max_len = length
            result = item
        elif length == max_len:
            result = item
    return (max_len, result)