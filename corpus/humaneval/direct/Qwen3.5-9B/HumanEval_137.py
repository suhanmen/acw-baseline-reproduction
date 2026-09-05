def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """
    def parse_value(val):
        if isinstance(val, (int, float)):
            return float(val)
        if isinstance(val, str):
            normalized = val.replace(',', '.')
            return float(normalized)
        return None

    val_a = parse_value(a)
    val_b = parse_value(b)

    if val_a == val_b:
        return None

    if a == b:
        return a

    if isinstance(a, str):
        return a
    elif isinstance(b, str):
        return b
    elif isinstance(a, float) and isinstance(b, int):
        if val_a > val_b:
            return a
        return b
    elif isinstance(a, int) and isinstance(b, float):
        if val_a > val_b:
            return a
        return b
    else:
        if val_a > val_b:
            return a
        return b