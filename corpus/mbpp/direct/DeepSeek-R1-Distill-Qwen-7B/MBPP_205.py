def inversion_elements(t):
    return tuple(-x - i - 2 for i, x in enumerate(t))