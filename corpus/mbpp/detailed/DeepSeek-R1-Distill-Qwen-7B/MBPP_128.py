def long_words(n, words):
    # Validate inputs
    def validate_inputs(n, words):
        if not isinstance(n, (int, float)):
            raise TypeError("n must be an integer or float")
        if not isinstance(words, list):
            raise TypeError("words must be a list")
        return True

    # Validate inputs and handle edge cases
    if not validate_inputs(n, words):
        raise TypeError("Invalid input")

    # If n is 0 or negative, all words will be included
    if n <= 0:
        return [word for word in words]

    # Get the lengths of all words
    word_lengths = get_word_lengths(words)

    # Filter words longer than n
    filtered_words = filter_words(n, words, word_lengths)

    return filtered_words

# Helper function to get lengths of words
def get_word_lengths(words):
    return [len(word) for word in words]

# Helper function to filter words based on length
def filter_words(n, words, word_lengths):
    return [word for word, length in zip(words, word_lengths) if length > n]

# Example usage:
# print(long_words(3, ["python", "is", "a", "programming", "language"]))
# Output: ['python', 'programming', 'language']