def most_occurrences(sentences):
    from collections import Counter
    words = []
    for sentence in sentences:
        words.extend(sentence.split())
    counter = Counter(words)
    if not counter:
        return ''
    return max(counter, key=counter.get)