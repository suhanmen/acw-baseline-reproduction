def group_keyvalue(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            result[key].append(value)
        else:
            result[key] = [value]
    return result