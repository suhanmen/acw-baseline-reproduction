def re_arrange(arr, n):
    pos = []
    neg = []
    for x in arr:
        if x >= 0:
            pos.append(x)
        else:
            neg.append(x)
    result = []
    i = 0
    j = 0
    while i < len(pos) and j < len(neg):
        result.append(neg[j])
        j += 1
        result.append(pos[i])
        i += 1
    while j < len(neg):
        result.append(neg[j])
        j += 1
    while i < len(pos):
        result.append(pos[i])
        i += 1
    return result