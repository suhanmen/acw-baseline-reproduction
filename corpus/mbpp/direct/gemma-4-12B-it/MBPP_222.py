def check_type(tup):
    if not tup:
        return True
    first_type = type(tup[0])
    for item in tup:
        if type(item) != first_type:
            return False
    return True