def find_Nth_Digit(a, b, n):
    if a == 0 or b == 0:
        return 0
    result = ""
    i = 0
    remainder = a
    while True:
        remainder *= 10
        digit = remainder // b
        result += str(digit)
        remainder = remainder % b
        if remainder == 0:
            break
        if len(result) > n:
            break
    return int(result[n])