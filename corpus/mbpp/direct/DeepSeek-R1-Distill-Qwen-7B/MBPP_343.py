def dig_let(s):
    # Count the number of digits and letters in the string
    digits = 0
    letters = 0
    for c in s:
        if c.isdigit():
            digits += 1
        elif c.isalpha():
            letters += 1
    return (letters, digits)