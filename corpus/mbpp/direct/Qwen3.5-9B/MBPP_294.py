def max_val(items):
    max_val = None
    max_type = None
    for item in items:
        if max_val is None or type(item).__name__ != type(max_val).__name__:
            if max_val is None or item > max_val:
                max_val = item
                max_type = type(item)
        elif max_val is not None:
            try:
                if item > max_val:
                    max_val = item
            except TypeError:
                pass
    return max_val