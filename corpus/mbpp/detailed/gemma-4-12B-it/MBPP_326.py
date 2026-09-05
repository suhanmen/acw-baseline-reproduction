import collections
import re
from typing import List

def most_occurrences(strings: List[str]) -> str:
    """
    Identifies the word that appears most frequently across a list of strings.

    The function treats words as sequences of alphanumeric characters, 
    ignoring punctuation. It is case-insensitive for counting purposes 
    but returns the word in its first-encountered lowercase form.

    Args:
        strings (List[str]): A list of sentences or phrases.

    Returns:
        str: The most frequent word found in the list.

    Raises:
        ValueError: If the input list is empty or contains no valid words.
    """
    # Validate input type
    if not isinstance(strings, list):
        raise ValueError("Input must be a list of strings.")

    # Handle empty list edge case
    if not strings:
        raise ValueError("The input list is empty.")

    # Dictionary to store frequency of words
    # Key: word (lowercase), Value: integer count
    word_counts = collections.defaultdict(int)

    # To maintain the first occurrence for tie-breaking (if required)
    # or simply to keep track of which words we've seen.
    # However, the requirement doesn't specify tie-breaking, 
    # so we'll return the first one encountered among the max counts.
    first_appearance_order = []

    for text in strings:
        # Validate that each element in the list is a string
        if not isinstance(text, str):
            raise ValueError(f"Expected string in list, got {type(text).__name__}")

        # Clean the text:
        # 1. Convert to lowercase to ensure 'UTS' and 'uts' are counted together
        # 2. Use regex to find all alphanumeric sequences (words)
        # This effectively removes punctuation like periods, commas, etc.
        cleaned_text = text.lower()
        words = re.findall(r'\b\w+\b', cleaned_text)

        for word in words:
            # Skip empty strings if regex captures any
            if not word:
                continue

            if word_counts[word] == 0:
                first_appearance_order.append(word)

            word_counts[word] += 1

    # Handle case where list contains strings but no actual words (e.g., ["!!!", "???"])
    if not word_counts:
        raise ValueError("No valid words were found in the provided strings.")

    # Find the maximum frequency value
    max_frequency = 0
    for count in word_counts.values():
        if count > max_frequency:
            max_frequency = count

    # Identify all words that have that maximum frequency
    candidates = []
    for word in first_appearance_order:
        if word_counts[word] == max_frequency:
            candidates.append(word)

    # The problem implies a single answer. 
    # In case of ties, we return the one that appeared first in the sequence.
    if candidates:
        return candidates[0]

    # This part should technically not be reached due to the check above
    raise ValueError("Failed to determine the most frequent word.")