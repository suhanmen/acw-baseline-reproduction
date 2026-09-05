def even_or_odd(hex_str):
    # Convert the hexadecimal string to an integer
    num = int(hex_str, 16)
    # Check if the number is even or odd
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"