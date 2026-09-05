def multiply_int(a, b):
    if b == 0:
        return 0
    if b < 0:
        return -multiply_int(a, -b)
    return a + multiply_int(a, b - 1)