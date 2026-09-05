def list_split(lst, n):
    result = [[] for _ in range(n)]
    for i, elem in enumerate(lst):
        result[i % n].append(elem)
    return result