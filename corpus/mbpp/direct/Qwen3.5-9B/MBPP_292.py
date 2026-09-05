def find(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return int(a // b)