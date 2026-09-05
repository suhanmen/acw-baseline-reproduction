def check_type(t):
    if len(t) == 0:
        return True
    first_type = type(t[0])
    return all(isinstance(item, first_type) for item in t)