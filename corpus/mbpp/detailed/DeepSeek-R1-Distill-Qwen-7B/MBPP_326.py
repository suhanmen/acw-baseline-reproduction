def most_occurrences(strings):
    if not strings:
        return None

    word_counts = {}

    # Count word occurrences
    for string in strings:
        words = string.split()
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

    # Find the maximum count
    if not word_counts:
        return None

    max_count = max(word_counts.values())
    highest_count_words = [word for word, count in word_counts.items() if count == max_count]

    # Return the first word with the highest count
    return highest_count_words[0]