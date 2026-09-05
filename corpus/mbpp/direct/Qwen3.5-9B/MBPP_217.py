def first_Repeated_Char(s: str) -> str:
    seen = set()
    for ch in s:
        if ch in seen:
            return ch
        seen.add(ch)
    return '\0'