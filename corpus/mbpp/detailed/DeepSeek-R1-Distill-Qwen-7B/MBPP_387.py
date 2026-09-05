def even_or_odd(hex_str):
    # Validate the input
    allowed_chars = set("0123456789ABCDEFabcdef")
    if any(c not in allowed_chars for c in hex_str):
        return "Invalid Input"

    # Convert hexadecimal string to decimal
    try:
        decimal_value = int(hex_str, 16)
    except ValueError:
        return "Invalid Input"

    # Check if the number is even or odd
    if decimal_value % 2 == 0:
        return "Even"
    else:
        return "Odd"