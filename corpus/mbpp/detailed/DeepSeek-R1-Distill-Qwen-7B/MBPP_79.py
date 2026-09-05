def word_len(word):
    # Check if the input is a string
    if not isinstance(word, str):
        raise ValueError("Input must be a string.")

    # Handle empty string case
    if len(word) == 0:
        return False  # An empty string has even length (0)

    # Calculate the length of the word
    word_length = len(word)

    # Check if the length is odd
    if word_length % 2 == 1:
        return True
    else:
        return False