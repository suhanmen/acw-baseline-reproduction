def group_keyvalue(keyvalue_pairs):
    result = {}
    for key, value in keyvalue_pairs:
        if key not in result:
            result[key] = []
        result[key].append(value)
    return result