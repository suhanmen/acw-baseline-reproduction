def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """

    # Validate input
    if not isinstance(words, list) or not all(isinstance(word, str) for word in words):
        return ""

    if not words:
        return ""

    # If there's only one word, return it
    if len(words) == 1:
        return words[0]

    # Calculate unique characters for each word and store along with the word
    word_info = []
    for word in words:
        unique_chars = len(set(word))
        word_info.append((unique_chars, word))

    # Find the maximum number of unique characters
    max_unique = max(unique_chars for unique_chars, _ in word_info)

    # Filter words that have the maximum unique characters
    max_words = [word for unique_chars, word in word_info if unique_chars == max_unique]

    # Return the lexicographically smallest word among those with maximum unique characters
    return min(max_words)