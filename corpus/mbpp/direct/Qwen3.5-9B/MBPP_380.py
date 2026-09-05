def multi_list(m, n):
    result = []
    for i in range(m):
        row = [0]
        for j in range(n):
            row.append(i * j)
        result.append(row)
    return result