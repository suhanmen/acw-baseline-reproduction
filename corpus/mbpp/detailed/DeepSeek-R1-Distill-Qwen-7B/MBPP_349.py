def check(s):
    # Check if input is a string
    if not isinstance(s, str):
        return "No"

    # If the string is empty, it's not binary
    if len(s) == 0:
        return "No"

    # Check each character in the string
    for char in s:
        if char not in ('0', '1'):
            return "No"

    # If all characters are 0 or 1
    return "Yes"