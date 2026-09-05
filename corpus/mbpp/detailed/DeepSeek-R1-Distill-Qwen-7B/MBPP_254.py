def words_ae(s):
    words = s.split()
    valid_words = []

    for word in words:
        if word and word[0].lower() in ('a', 'e'):
            valid_words.append(word)

    return valid_words