import re

def find_long_word(text: str) -> list[str]:
    """
    Finds all five-character long words in the given string using regex.
    Words are defined as sequences of alphabetic characters bounded by non-word 
    characters or string boundaries.
    """
    # \b is a word boundary. [a-zA-Z] ensures we only match letters.
    # {5} ensures the length is exactly five.
    pattern = r'\b[a-zA-Z]{5}\b'
    return re.findall(pattern, text)