def start_withp(words):
    matches = []
    for word in words:
        if word.startswith('p'):
            matches.append(word)
            if len(matches) == 2:
                break
    return matches