def is_num_keith(n: int) -> bool:
    if n <= 0:
        return False

    digits = []
    temp = n
    while temp > 0:
        digits.append(temp % 10)
        temp //= 10
    digits.reverse()

    a, b = digits[0], digits[1] if len(digits) > 1 else 0

    for i in range(2, len(digits)):
        c = a + b
        if c != digits[i]:
            return False
        a, b = b, c

    return True