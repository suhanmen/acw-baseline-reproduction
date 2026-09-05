def upper_ctr(s: str) -> int:
    return sum(1 for char in s if char.isupper())