def check_value(d, target):
    if not d:
        return False
    return all(v == target for v in d.values())