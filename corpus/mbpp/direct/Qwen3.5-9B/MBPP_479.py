def first_digit(n):
    n = abs(n)
    while n >= 10:
        n //= 10
    return n