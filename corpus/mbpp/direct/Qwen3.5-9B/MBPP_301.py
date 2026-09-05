def dict_depth(d):
    if not isinstance(d, dict):
        return 0
    depth = 0
    for value in d.values():
        if isinstance(value, dict):
            depth = max(depth, dict_depth(value) + 1)
        else:
            if depth == 0:
                depth = 1
    return depth