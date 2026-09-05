def minimum(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numeric values.")
    if a == b:
        return a
    if a < b:
        return a
    else:
        return b