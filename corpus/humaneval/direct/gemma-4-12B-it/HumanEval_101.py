import re

def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.

    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # Use regex to split by one or more occurrences of comma or space
    # Filter out empty strings in case of leading/trailing punctuation or double separators
    return [word for word in re.split(r'[,\s]+', s) if word]