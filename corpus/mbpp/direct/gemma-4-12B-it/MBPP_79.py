def word_len(word: str) -> bool:
    """
    Checks whether the length of the word is odd.

    Args:
        word (str): The string to check.

    Returns:
        bool: True if the length is odd, False otherwise.
    """
    return len(word) % 2 != 0

if __name__ == "__main__":
    assert word_len("Hadoop") == False
    assert word_len("great") == True
    assert word_len("structure") == True