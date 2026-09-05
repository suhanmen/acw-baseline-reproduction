def long_words(n, text):
    """
    Shortlists words from a given text that are strictly longer than n characters.

    Args:
        n (int): The length threshold.
        text (str): The input string containing words separated by spaces.

    Returns:
        list: A list of words with length greater than n.
    """
    words = text.split()
    return [word for word in words if len(word) > n]

if __name__ == "__main__":
    assert long_words(3, "python is a programming language") == ['python', 'programming', 'language']
    assert long_words(2, "writing a program") == ['writing', 'program']
    assert long_words(5, "sorting list") == ['sorting']