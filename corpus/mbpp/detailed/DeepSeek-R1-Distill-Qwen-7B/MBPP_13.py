def count_common(words_list):
    # Step 1: Input Validation
    if not isinstance(words_list, list) or any(not isinstance(word, str) for word in words_list):
        return "Invalid input: must be a list of strings"

    # Step 2: Handle empty list
    if not words_list:
        return []

    # Step 3: Count the words
    word_counts = {}
    for word in words_list:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Step 4: Convert to list of tuples
    word_count_list = [(word, count) for word, count in word_counts.items()]

    # Step 5: Sort the list of tuples
    # First by count descending, then by the first occurrence ascending
    word_count_list.sort(key=lambda x: (-x[1], x[0]))

    # Step 6: Return the sorted list
    return word_count_list