def number_of_substrings(s):
    if not isinstance(s, str) or len(s) == 0:
        return 0
    n = len(s)
    return n * (n + 1) // 2