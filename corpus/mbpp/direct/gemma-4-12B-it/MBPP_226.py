def odd_values_string(s: str) -> str:
    """
    Removes characters which have odd index values of a given string.
    In Python, indices are 0-based, so 0 is even and 1 is odd.
    Therefore, it keeps characters at indices 0, 2, 4, etc.
    """
    return s[::2]

if __name__ == "__main__":
    assert odd_values_string('abcdef') == 'ace'
    assert odd_values_string('python') == 'pto'
    assert odd_values_string('data') == 'dt'