def find_Max_Len_Even(words_str: str) -> str:
    words = words_str.split()
    max_even_word = None
    max_len = -1

    for word in words:
        if len(word) % 2 == 0:
            if len(word) > max_len:
                max_len = len(word)
                max_even_word = word

    if max_even_word is None:
        return "-1"
    return max_even_word