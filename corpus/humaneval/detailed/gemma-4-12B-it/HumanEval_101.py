import re
from typing import List

def words_string(s: str) -> List[str]:
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.

    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """

    # Validate input type
    if not isinstance(s, str):
        raise TypeError(f"Input must be a string, received {type(s).__name__}")

    # Handle the edge case of an empty string immediately
    if not s:
        return []

    # Step 1: Define the delimiters. 
    # The problem specifies commas and spaces as separators.
    # We use a regular expression to capture any sequence of one or more 
    # commas or spaces as a single delimiter.
    delimiter_pattern = r'[,\s]+'

    # Step 2: Perform the split.
    # re.split will split the string based on the pattern provided.
    # This handles multiple consecutive delimiters (e.g., ", ") automatically.
    raw_split_list = re.split(delimiter_pattern, s)

    # Step 3: Clean up the resulting list.
    # re.split can sometimes leave empty strings in the list if the 
    # string starts or ends with a delimiter.
    cleaned_words = []
    for item in raw_split_list:
        # Strip leading/trailing whitespace from the word just in case,
        # though the regex should handle most of this.
        trimmed_word = item.strip()

        # Only add to the result if the word is not empty.
        if trimmed_word != "":
            cleaned_words.append(trimmed_word)

    return cleaned_words

# Note: The logic ensures that "Hi, my name" results in ["Hi", "my", "name"]
# by treating ", " (comma followed by space) as a continuous delimiter 
# block rather than two separate delimiters that would produce an empty string.