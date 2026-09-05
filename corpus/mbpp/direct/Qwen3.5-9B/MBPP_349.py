def check(s: str) -> str:
    return "Yes" if all(c in '01' for c in s) else "No"