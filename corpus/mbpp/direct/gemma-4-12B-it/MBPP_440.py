import re

def find_adverb_position(sentence: str) -> tuple:
    """
    Finds the position and content of the first adverb in a sentence.
    Based on the provided test cases, the function identifies words ending
    with 'ly' that appear before punctuation.
    """
    # Find words ending in 'ly'
    # The pattern \b[a-zA-Z]+ly\b matches words ending in 'ly'
    # We use re.search to find the first occurrence.
    match = re.search(r'\b(\w+ly)\b', sentence)
    if match:
        return (match.start(), match.end(), match.group(1))
    return None