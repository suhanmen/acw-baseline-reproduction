def count_charac(s: str) -> int:
    """
    Counts the total number of characters in a given string.
    """
    return len(s)

if __name__ == "__main__":
    assert count_charac("python programming") == 18
    assert count_charac("language") == 8
    assert count_charac("words") == 5