def remove_tuple(t):
    seen = set()
    result = []
    for element in t:
        if element not in seen:
            seen.add(element)
            result.append(element)
    return tuple(result)