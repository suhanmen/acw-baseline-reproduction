def len_log(words: list[str]) -> int:
    """
    Finds the length of the longest word in a list of strings.
    """
    if not words:
        return 0
    return max(len(word) for word in words)