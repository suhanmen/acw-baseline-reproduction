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
    # Handle cases where a or b is a string representing a number
    try:
        float_a = float(a)
        float_b = float(b)
    except ValueError:
        # If conversion to float fails, treat as non-numeric
        float_a = float_b = None

    if float_a is None and float_b is None:
        return None  # Both are non-numeric

    # Compare as per numeric values if possible
    if float_a is not None and float_b is not None:
        if float_a > float_b:
            return a if isinstance(a, str) else float_a
        elif float_a < float_b:
            return b if isinstance(b, str) else float_b
        else:
            return None
    else:
        # Return non-numeric type if one of them is non-numeric
        if isinstance(a, str):
            return a
        elif isinstance(b, str):
            return b
        else:
            return None