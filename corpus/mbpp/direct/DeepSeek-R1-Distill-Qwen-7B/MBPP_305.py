def start_withp(words):
    for word_pair in words.split(', '):
        parts = word_pair.split()
        if len(parts) == 2 and parts[0].startswith('p') and parts[1].startswith('p'):
            return (parts[0], parts[1])
    return None