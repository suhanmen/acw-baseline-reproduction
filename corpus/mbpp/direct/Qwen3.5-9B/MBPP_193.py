def remove_tuple(t):
    seen = set()
    result = []
    for item in t:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return tuple(result)