def check_Equality(s: str) -> str:
    if not s:
        return "Not Equal"
    return "Equal" if s[0] == s[-1] else "Not Equal"