def upper_ctr(s: str) -> int:
    return sum(1 for c in s if c.isupper())