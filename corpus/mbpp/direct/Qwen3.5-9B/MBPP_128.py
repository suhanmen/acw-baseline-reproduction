def long_words(n, words_str):
    words = words_str.split()
    return [word for word in words if len(word) > n]