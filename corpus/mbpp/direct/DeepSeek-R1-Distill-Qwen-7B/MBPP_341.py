def set_to_tuple(s):
    if not isinstance(s, set):
        raise TypeError("Argument must be a set")
    return tuple(sorted(s))