def decimal_to_Octal(n):
    if n == 0:
        return '0'
    octal = ''
    while n > 0:
        octal = str(n % 8) + octal
        n = n // 8
    return octal

assert decimal_to_Octal(10) == 12
assert decimal_to_Octal(2) == 2
assert decimal_to_Octal(33) == 41