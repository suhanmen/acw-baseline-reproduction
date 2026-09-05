def is_lower(s: str) -> str:
    """
    Converts the given string to lower case.
    """
    return s.lower()

if __name__ == "__main__":
    assert is_lower("InValid") == "invalid"
    assert is_lower("TruE") == "true"
    assert is_lower("SenTenCE") == "sentence"