def tuple_int_str(t: tuple) -> tuple:
    return tuple(tuple(int(inner) for inner in outer) for outer in t)