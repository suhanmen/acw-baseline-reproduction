def concatenate_elements(tup):
    if not tup:
        return ()
    result = []
    for i in range(len(tup) - 1):
        result.append(tup[i] + tup[i + 1])
    return tuple(result)