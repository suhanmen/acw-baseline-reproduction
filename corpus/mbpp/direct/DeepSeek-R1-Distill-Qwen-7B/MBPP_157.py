def encode_list(x):
    if not isinstance(x, list):
        raise TypeError("Expected list as input")

    result = []
    prev = x[0]
    count = 1

    for elem in x[1:]:
        if elem == prev:
            count += 1
        else:
            result.append([count, prev])
            prev = elem
            count = 1
    result.append([count, prev])

    return result