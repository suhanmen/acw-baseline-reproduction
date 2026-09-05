def modified_encode(x):
    if not x:
        return []

    if isinstance(x, str):
        iterator = iter(x)
    else:
        iterator = iter(x)

    current = None
    count = 0
    result = []

    for elem in iterator:
        if elem == current:
            count += 1
        else:
            if current is not None:
                if count == 1:
                    result.append(current)
                else:
                    result.append([count, current])
            current = elem
            count = 1

    if current is not None:
        if count == 1:
            result.append(current)
        else:
            result.append([count, current])

    return result