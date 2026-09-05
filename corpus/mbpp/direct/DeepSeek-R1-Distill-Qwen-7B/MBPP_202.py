def remove_even(s):
    # Remove even-indexed characters (0-based) and keep odd-indexed characters (1-based)
    return ''.join([s[i] for i in range(1, len(s), 2)])