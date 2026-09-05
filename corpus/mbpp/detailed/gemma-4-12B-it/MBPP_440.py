import re
from typing import List, Tuple, Optional


def find_adverb_position(sentence: str) -> Tuple[int, int, str]:
    """
    Identifies the position and the word of the first adverb found in a sentence.
    Based on the provided assertions, the "adverb" is identified as the first
    word in the string that ends with 'ly' before punctuation or spaces.

    The function returns a tuple of (start_index, end_index, adverb_word).

    Args:
        sentence (str): The input string to search.

    Returns:
        Tuple[int, int, str]: The start index, end index (exclusive), and the word.

    Raises:
        ValueError: If no adverb is found or input is invalid.
        TypeError: If input is not a string.
    """
    # Input Validation
    if not isinstance(sentence, str):
        raise TypeError(f"Expected string input, got {type(sentence).__name__}")

    if not sentence.strip():
        raise ValueError("Input sentence is empty or only contains whitespace.")

    # Define the logic for identifying an adverb based on the provided examples.
    # The examples show words like "clearly!!", "seriously!!", "unfortunately!!"
    # where the adverb is the alphabetic part ending in 'ly'.
    # We look for a sequence of letters ending in 'ly' at the start of the string.

    # We use a regular expression to find the first sequence of letters ending in 'ly'
    # followed by non-alphabetic characters (like '!!') or whitespace.
    # The pattern looks for word characters, specifically ensuring it ends with 'ly'.
    # We use a capturing group to isolate the word itself.

    # Pattern explanation:
    # ^          : Start of string
    # ([a-zA-Z]+ly) : Group 1: One or more letters ending in 'ly'
    # [^a-zA-Z]* : Zero or more non-alphabetic characters (like '!!')
    # \s*        : Optional trailing whitespace

    # Note: The assertions imply the 'ly' word is at the very beginning.
    pattern = r"^([a-zA-Z]+ly)[^a-zA-Z]*\s*"

    match = re.search(pattern, sentence)

    if match:
        # The full match includes the '!!' or spaces.
        # The first capturing group is just the 'ly' word.
        full_match_text = match.group(0)
        adverb_word = match.group(1)

        # The requirement asks for the position of the adverb.
        # Looking at the assertions:
        # "clearly!! we can see" -> (0, 7, 'clearly')
        # 'clearly' is 7 characters long. Indices 0 to 7.
        # This means the end index is the length of the adverb_word itself,
        # NOT the position of the punctuation.

        start_index = match.start(1)
        end_index = match.end(1)

        return (start_index, end_index, adverb_word)

    # If the logic above is too strict for general cases (adverbs not at start),
    # we can fall back to searching the whole string.
    # However, based strictly on the assertions provided, the word is at index 0.

    # Fallback: Search for any word ending in 'ly'
    # This is used if the adverb is not at the very start.
    fallback_pattern = r"\b([a-zA-Z]+ly)\b"
    fallback_match = re.search(fallback_pattern, sentence)

    if fallback_match:
        start_idx = fallback_match.start(1)
        end_idx = fallback_match.end(1)
        word = fallback_match.group(1)
        return (start_idx, end_idx, word)

    # If no adverb is found
    raise ValueError("No adverb ending in 'ly' was found in the provided sentence.")


if __name__ == "__main__":
    # These are the provided assertions to satisfy.
    # The logic ensures 'clearly!!' returns (0, 7, 'clearly')
    # because 'clearly' is 7 characters.

    assert find_adverb_position("clearly!! we can see the sky") == (0, 7, 'clearly')
    assert find_adverb_position("seriously!! there are many roses") == (0, 9, 'seriously')
    assert find_adverb_position("unfortunately!! sita is going to home") == (0, 13, 'unfortunately')