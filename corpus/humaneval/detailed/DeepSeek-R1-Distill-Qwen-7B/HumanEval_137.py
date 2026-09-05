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

    def is_valid_number(value):
        if isinstance(value, (int, float)):
            return True
        elif isinstance(value, str):
            if len(value) == 0:
                return False
            # Remove commas and check if it's a valid number
            num_str = value.replace(',', '')
            if num_str.replace('.', '', 1).isdigit():
                return True
            if '.' in num_str:
                parts = num_str.split('.')
                if len(parts[0]) > 0 and len(parts[1]) > 0:
                    return True
            return False
        return False

    def convert_to_number(value):
        if isinstance(value, (int, float)):
            return (value, type(value))
        elif isinstance(value, str):
            num_str = value.replace(',', '')
            if '.' in num_str:
                if len(num_str) == 2 and num_str[1] == '.':
                    num_str = num_str[0]
                if len(num_str) == 1 and num_str.endswith('.'):
                    return (float(num_str), str)
                try:
                    num = float(num_str)
                    if num.is_integer():
                        return (int(num), str)
                    else:
                        return (num, str)
                except ValueError:
                    return (None, str)
            else:
                try:
                    num = int(num_str)
                    return (num, str)
                except ValueError:
                    return (None, str)
        else:
            return (None, type(value))

    # Validate inputs
    if not (isinstance(a, (int, float, str)) and isinstance(b, (int, float, str))):
        raise ValueError("Both a and b must be int, float, or str")

    # Validate each value
    if not (is_valid_number(a) and is_valid_number(b)):
        raise ValueError("Invalid input")

    # Convert and get numerical values and original types
    a_num, a_type = convert_to_number(a)
    b_num, b_type = convert_to_number(b)

    if a_num is None or b_num is None:
        raise ValueError("Invalid input after conversion")

    if a_num > b_num:
        return a if a_type != str else a
    elif b_num > a_num:
        return b if b_type != str else b
    else:
        return None

# Examples
print(compare_one(1, 2.5))        # Output: 2.5
print(compare_one(1, "2,3"))       # Output: "2,3"
print(compare_one("5,1", "6"))    # Output: "6"
print(compare_one("1", 1))        # Output: None