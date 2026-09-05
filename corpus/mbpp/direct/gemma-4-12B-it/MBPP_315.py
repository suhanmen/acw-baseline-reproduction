def find_Max_Len_Even(s: str) -> str:
    """
    Finds the first maximum length even-length word in a string.
    If no even-length words exist, returns "-1".
    """
    words = s.split()
    max_len = -1
    result = "-1"

    for word in words:
        # Clean word of punctuation if necessary (though standard split is usually enough)
        # The requirements imply words are separated by spaces.
        word_len = len(word)
        if word_len % 2 == 0:
            if word_len > max_len:
                max_len = word_len
                result = word

    return result