def ascii_value_string(s: str) -> int:
    """Returns the ASCII value of the first character in the string."""
    if not s:
        raise ValueError("Input string must not be empty.")
    return ord(s[0])