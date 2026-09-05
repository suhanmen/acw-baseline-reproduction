def even_or_odd(hex_str):
    num = int(hex_str, 16)
    return "Even" if num % 2 == 0 else "Odd"