def remove_tuple(t):
    seen = set()
    result = []
    for element in t:
        if element not in seen:
            result.append(element)
            seen.add(element)
    return tuple(result)