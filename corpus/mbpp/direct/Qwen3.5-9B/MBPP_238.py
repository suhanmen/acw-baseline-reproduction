def number_of_substrings(s: str) -> int:
    n = len(s)
    return n * (n + 1) // 2