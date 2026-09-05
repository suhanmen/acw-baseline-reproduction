def string_to_list(s):
    """
    Converts a string into a list of words, handling various edge cases.

    Args:
        s (str): The input string to be converted into a list.

    Returns:
        list: A list of words from the input string.

    Raises:
        ValueError: If the input is not a string.
    """
    # Helper function to remove trailing punctuation from each word
    def remove_trailing_punctuation(word):
        # Iterate from the end of the word to find the first non-punctuation character
        for i in range(len(word)-1, -1, -1):
            if not word[i].isalpha():
                return word[:i]
        return word

    # Validate the input
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")

    # Split the string into words, handling multiple spaces
    words = s.split()

    # Remove trailing punctuation from each word and filter out empty strings
    cleaned_words = []
    for word in words:
        # Remove trailing punctuation
        cleaned_word = remove_trailing_punctuation(word)
        if cleaned_word:
            cleaned_words.append(cleaned_word)

    return cleaned_words

# Example usage and assertions
def test_string_to_list():
    assert string_to_list("python programming") == ['python', 'programming']
    assert string_to_list("lists tuples strings") == ['lists', 'tuples', 'strings']
    assert string_to_list("write a program") == ['write', 'a', 'program']
    assert string_to_list("") == []
    assert string_to_list("   ") == []
    assert string_to_list("hello,world") == ['hello,world']
    assert string_to_list("hello world.") == ['hello', 'world']
    print("All test cases passed.")

test_string_to_list()