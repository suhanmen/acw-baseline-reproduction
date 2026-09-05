def add_nested_tuples(t1: tuple, t2: tuple) -> tuple:
    result = []
    for x, y in zip(t1, t2):
        result.append(tuple(a + b for a, b in zip(x, y)))
    return tuple(result)