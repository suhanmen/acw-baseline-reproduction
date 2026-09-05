def and_tuples(t1, t2):
    return tuple(a & b for a, b in zip(t1, t2))