def number_of_substrings(s: str) -> int:
    """
    Returns the number of non-empty substrings of a given string.
    The number of non-empty substrings for a string of length n is n*(n+1)/2.
    """
    n = len(s)
    return n * (n + 1) // 2

if __name__ == "__main__":
    assert number_of_substrings("abc") == 6
    assert number_of_substrings("abcd") == 10
    assert number_of_substrings("abcde") == 15