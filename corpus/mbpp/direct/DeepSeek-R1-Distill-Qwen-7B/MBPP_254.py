def words_ae(s):
    words = s.split()
    result = []
    for word in words:
        if word.startswith(('a', 'e')):
            if len(word) >= 2:  # Ensure the word has at least two characters
                result.append(word)
    return result