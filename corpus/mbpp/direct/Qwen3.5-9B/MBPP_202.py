def remove_even(s):
    return ''.join(c for i, c in enumerate(s) if i % 2 != 0)