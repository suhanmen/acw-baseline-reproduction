def and_tuples(a, b):
    return tuple(a[i] - b[i] if a[i] > b[i] else 0 for i in range(len(a)))