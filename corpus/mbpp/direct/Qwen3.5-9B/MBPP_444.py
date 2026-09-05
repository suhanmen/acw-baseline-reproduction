def trim_tuple(tuple_list, k):
    result = []
    for t in tuple_list:
        trimmed = t[k:]
        result.append(trimmed)
    return str(result)