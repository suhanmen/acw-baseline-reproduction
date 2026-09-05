python
def multiply_int(a, b):
    if b < 0:
        return -multiply_int(a, -b)
    result = 0
    for _ in range(b):
        result += a
    return result