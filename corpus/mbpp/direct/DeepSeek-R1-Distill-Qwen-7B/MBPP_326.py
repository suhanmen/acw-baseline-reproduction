def most_occurrences(strings):
    from collections import defaultdict

    # Create a dictionary to count occurrences
    counts = defaultdict(int)

    # Count each word occurrence
    for string in strings:
        words = string.split()
        for word in words:
            counts[word] += 1

    # Find the word(s) with the maximum occurrence
    max_count = max(counts.values(), default=0)
    for word, count in counts.items():
        if count == max_count:
            return word
    return ''