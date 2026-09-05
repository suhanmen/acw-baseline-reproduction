import re

def check_char(s):
    if len(s) == 0:
        return "Invalid"
    pattern = r'.^(\w)\1$'
    match = re.match(pattern, s)
    if match:
        return "Valid"
    else:
        return "Invalid"

# Example usage:
# print(check_char("abba"))  # Output: "Valid"
# print(check_char("a"))     # Output: "Valid"
# print(check_char("abcd"))  # Output: "Invalid"