import re
from typing import Union, Optional

def _validate_input(s: Union[str, None, int, float, list, dict, tuple, set]) -> None:
    """
    Validates that the input is a non-empty string.
    Raises a TypeError if the type is incorrect.
    Raises a ValueError if the string is empty.
    """
    if not isinstance(s, str):
        raise TypeError(
            f"Invalid input type: expected str, got {type(s).__name__}. "
            "The function requires a string of words."
        )

    if len(s) == 0:
        raise ValueError(
            "Invalid input value: the input string cannot be empty. "
            "Provide a non-empty string containing sentences."
        )

def _normalize_sentence_text(s: str) -> str:
    """
    Normalizes the input string by collapsing multiple whitespace characters
    into a single space and stripping leading/trailing whitespace.

    Args:
        s: The input string to normalize.

    Returns:
        The normalized string with single spaces between words.
    """
    # Replace one or more whitespace characters with a single space
    normalized = re.sub(r'\s+', ' ', s)
    # Strip leading and trailing whitespace
    return normalized.strip()

def _extract_sentences(s: str) -> list[str]:
    """
    Splits the normalized input string into individual sentences.
    Sentences are considered to end with '.', '?', or '!'.
    The split preserves any text following these delimiters if present,
    but for this problem, we assume standard sentence structures where
    the delimiter marks the end of a sentence.

    Since the problem states sentences are delimited by '.', '?', or '!',
    we can split the string by these characters and then clean up the resulting parts.
    However, a more robust approach for "I am here." vs "I am here..!" is to treat
    the delimiter as a word boundary marker.

    We will use a regex approach to split by the delimiters, keeping the delimiters
    temporarily to identify sentence endings, or simply split by the regex pattern
    for one or more of the delimiters.

    Strategy:
    1. Use regex to find all sentences. A sentence is a sequence of characters
       that starts after a delimiter (or the beginning of the string) and ends
       just before the next delimiter.
    2. We will split the string using the pattern r'[.?!]+' which matches one or
       more of the delimiter characters.

    Args:
        s: The normalized string.

    Returns:
        A list of sentences (strings). Empty strings resulting from trailing
        delimiters are filtered out.
    """
    # Split by one or more of the delimiter characters
    # This regex finds all occurrences of '.', '?', or '!' and splits there.
    # Example: "Hello. How are you?" -> ["Hello", " How are you", ""]
    # Note: re.split includes the separators if a capturing group is used, but 
    # here we want to discard them.

    raw_sentences = re.split(r'[.?!]+', s)

    # Filter out empty strings that might result from trailing punctuation
    sentences = [sentence for sentence in raw_sentences if sentence.strip()]

    return sentences

def _is_sentence_bored(sentence: str) -> bool:
    """
    Determines if a given sentence starts with the word "I".
    The check is case-sensitive based on the examples ("I" vs "i").

    Args:
        sentence: A single sentence string.

    Returns:
        True if the sentence starts with the word "I" (case-sensitive), False otherwise.
    """
    # Strip leading whitespace to ensure we are checking the first word correctly
    cleaned_sentence = sentence.strip()

    if not cleaned_sentence:
        return False

    # Split the sentence into words
    words = cleaned_sentence.split()

    if not words:
        return False

    first_word = words[0]

    # Check if the first word is exactly "I"
    return first_word == "I"

def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.

    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    # Step 1: Validate the input
    _validate_input(S)

    # Step 2: Normalize the input string
    normalized_text = _normalize_sentence_text(S)

    # Step 3: Extract individual sentences
    sentences = _extract_sentences(normalized_text)

    # Step 4: Iterate through sentences and count boredoms
    boredom_count = 0

    for sentence in sentences:
        # Check if the current sentence is a boredom
        if _is_sentence_bored(sentence):
            boredom_count += 1

    return boredom_count