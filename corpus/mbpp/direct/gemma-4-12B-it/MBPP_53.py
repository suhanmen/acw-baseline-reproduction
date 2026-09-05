def check_Equality(s: str) -> str:
    """
    Checks whether the first and last characters of a given string are equal.
    Returns "Equal" if they are, otherwise returns "Not Equal".
    """
    if not s:
        return "Not Equal"

    if s[0] == s[-1]:
        return "Equal"
    else:
        return "Not Equal"

if __name__ == "__main__":
    assert check_Equality("abcda") == "Equal"
    assert check_Equality("ab") == "Not Equal"
    assert check_Equality("mad") == "Not Equal"