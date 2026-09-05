def modified_encode(data):
    res = []
    i = 0
    n = len(data)
    while i < n:
        item = data[i]
        count = 1
        while i + count < n and data[i + count] == item:
            count += 1

        if count == 2:
            res.append([2, item])
        else:
            for _ in range(count):
                res.append(item)
        i += count
    return res