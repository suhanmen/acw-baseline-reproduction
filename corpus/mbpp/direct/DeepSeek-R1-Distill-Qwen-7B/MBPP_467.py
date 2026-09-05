def decimal_to_Octal(n):
    if not isinstance(n, int):
        return None
    if n < 0:
        return None
    return str(int(n, 8))

# Example usage:
# print(decimal_to_Octal(10))  # Output: 12
# print(decimal_to_Octal(2))   # Output: 2
# print(decimal_to_Octal(33))  # Output: 41