def dict_depth(d):
    if not isinstance(d, dict):
        return 0
    return 1 + max((dict_depth(v) for v in d.values()), default=0)