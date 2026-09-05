from collections import Counter

def count_common(words):
    if not words:
        return []
    return Counter(words).most_common()