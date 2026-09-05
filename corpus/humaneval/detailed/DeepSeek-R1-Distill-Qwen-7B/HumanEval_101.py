def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.

    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # Handle the case where s is None or not a string
    if not isinstance(s, str) or s is None:
        return []

    # Trim whitespace from the beginning and end of s
    s = s.strip()

    # If after trimming, s is empty, return empty list
    if not s:
        return []

    # Replace commas with spaces and split into tokens
    tokens = s.replace(',', ' ').split()

    # Filter out any empty strings resulting from multiple separators
    words = [token for token in tokens if token]

    return words