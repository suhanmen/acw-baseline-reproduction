python
def find_Max_Len_Even(text):
    """
    Find the first maximum length of even word in the given text.

    Steps:
    1. Split the text into words.
    2. Validate the input to ensure it is a string and not empty.
    3. Split the text into words using whitespace as the delimiter.
    4. Filter out words that do not have even lengths.
    5. If there are no even-length words, return "-1".
    6. If there are even-length words, find the first word with the maximum length.
    7. Return this word. If no words are found, return "-1".
    """
    # Validate the input
    if not isinstance(text, str) or not text:
        return "-1"

    # Split the text into words
    words = text.split()

    # Filter words with even lengths
    even_length_words = [word for word in words if len(word) % 2 == 0]

    # If no words have even lengths, return "-1"
    if not even_length_words:
        return "-1"

    # Find the maximum length among even-length words
    max_length = max(len(word) for word in even_length_words)

    # Find all words with the maximum length
    max_words = [word for word in even_length_words if len(word) == max_length]

    # Return the first word with the maximum length
    return max_words[0]