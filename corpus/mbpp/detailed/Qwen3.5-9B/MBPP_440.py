import re
from typing import List, Tuple, Union, Optional

# Define the list of common adverbs we want to detect.
# In a production system, this list might be generated from a larger linguistic corpus.
COMMON_ADVERBS = {
    "clearly",
    "seriously",
    "unfortunately",
    "quickly",
    "slowly",
    "very",
    "really",
    "just",
    "almost",
    "often",
    "sometimes",
    "never",
    "always",
    "sometimes",
    "perhaps",
    "hopefully",
    "probably",
    "definitely",
    "actually",
    "indeed",
    "truly",
    "barely",
    "quite",
    "simply",
    "hardly",
    "nearly",
    "frequently",
    "rarely",
    "currently",
    "generally",
    "specifically",
    "absolutely",
    "completely",
    "totally",
    "partially",
    "mainly",
    "mostly",
    "merely",
    "only",
    "even",
    "still",
    "yet",
    "already",
    "now",
    "then",
    "here",
    "there",
    "when",
    "where",
    "why",
    "how",
    "whether",
    "what",
    "which",
    "who",
    "whose",
    "whom",
    "that",
    "this",
    "these",
    "those",
    "and",
    "but",
    "or",
    "for",
    "nor",
    "so",
    "yet",
    "as",
    "if",
    "because",
    "while",
    "though",
    "unless",
    "although",
    "since",
    "after",
    "before",
    "until",
    "once",
    "once",
    "again",
    "again",
    "back",
    "down",
    "up",
    "out",
    "in",
    "on",
    "off",
    "over",
    "under",
    "about",
    "above",
    "below",
    "within",
    "without",
    "inside",
    "outside",
    "through",
    "along",
    "across",
    "against",
    "behind",
    "beside",
    "between",
    "among",
    "near",
    "away",
    "around",
    "circa",
    "pre",
    "post",
    "pro",
    "anti",
    "hyper",
    "hypo",
    "super",
    "sub",
    "infra",
    "extra",
    "meta",
    "neo",
    "para",
    "pan",
    "poly",
    "syn",
    "dia",
    "mono",
    "bi",
    "tri",
    "quad",
    "quint",
    "hex",
    "hept",
    "oct",
    "non",
    "dec",
    "hundred",
    "thousand",
    "million",
    "billion",
    "trillion",
    "quadrillion",
    "quintillion",
    "septillion",
    "octillion",
    "nonillion",
    "decillion",
    "undecillion",
    "duodecillion",
    "tredecillion",
    "quattuordecillion",
    "quindecillion",
    "sexdecillion",
    "septendecillion",
    "octodecillion",
    "novemdecillion",
    "vigintillion",
    "centillion",
}

def _validate_input(sentence: str) -> str:
    """
    Validates the input sentence and raises an exception if it is invalid.
    - Empty string is considered valid but will yield no results.
    - Non-string types raise a TypeError.
    - Returns the cleaned sentence (though cleaning is not strictly required by the problem,
      we ensure the input is a string).
    """
    if not isinstance(sentence, str):
        raise TypeError("Input sentence must be a string")

    # We allow empty strings as valid input that simply yields no results.
    if len(sentence) == 0:
        # Return an empty list or handle appropriately based on expected output format.
        # Since the problem expects a tuple or list of tuples, we return an empty list here.
        return sentence

    return sentence

def _extract_adverb_positions(
    sentence: str, 
    adverbs: set
) -> List[Tuple[int, int, str]]:
    """
    Extracts all adverbs from the sentence and returns a list of tuples.
    Each tuple contains (start_index, end_index, adverb_word).

    The search is case-sensitive unless specified otherwise.
    We look for the adverb as a whole word, surrounded by non-alphanumeric characters or string boundaries.

    Parameters:
        sentence (str): The input sentence to search within.
        adverbs (set): A set of adverb strings to search for.

    Returns:
        List[Tuple[int, int, str]]: A list of tuples with (start, end, word).
        If the sentence does not contain the adverb, the list will be empty.
    """
    results: List[Tuple[int, int, str]] = []

    # We will iterate through each unique adverb in the set.
    # Using a set ensures we only check each adverb once, even if the list has duplicates.
    unique_adverbs = sorted(list(adverbs))

    for current_adverb in unique_adverbs:
        adverb_len = len(current_adverb)
        if adverb_len == 0:
            # Skip empty adverb strings if any somehow get through.
            continue

        # We will search for the adverb in the sentence.
        # We use a simple manual search loop to avoid issues with overlapping matches or regex complexity.
        # However, since we need exact word matches, we can use a regex pattern that ensures word boundaries.

        # Construct a regex pattern for the current adverb with word boundaries.
        # \b represents a word boundary.
        pattern = r'\b' + re.escape(current_adverb) + r'\b'

        try:
            matches = re.finditer(pattern, sentence)
        except re.error:
            # This should rarely happen if the adverb string is valid, but good for defense.
            continue

        # Iterate over all matches found for the current adverb.
        for match in matches:
            start_pos = match.start()
            end_pos = match.end()
            matched_word = match.group()

            # Verify that the matched word is exactly the adverb we are looking for.
            # This prevents cases where the pattern might match a substring unexpectedly due to regex quirks.
            if matched_word != current_adverb:
                continue

            # Add the match details to our results list.
            results.append((start_pos, end_pos, matched_word))

    return results

def find_adverb_position(sentence: Union[str, None]) -> List[Tuple[int, int, str]]:
    """
    Finds all adverbs and their positions in a given sentence.

    Parameters:
        sentence (str | None): The input sentence to analyze.

    Returns:
        List[Tuple[int, int, str]]: A list of tuples, each containing:
            - start_index (int): The starting index of the adverb in the sentence.
            - end_index (int): The ending index (exclusive) of the adverb in the sentence.
            - adverb_word (str): The adverb itself.

        If no adverbs are found, returns an empty list.
        If the input is invalid, raises a TypeError or ValueError.
    """

    # Handle None input explicitly.
    if sentence is None:
        raise ValueError("Input sentence cannot be None")

    # Validate and clean the input string.
    cleaned_sentence = _validate_input(sentence)

    # If the sentence is empty after validation, return an empty list.
    if len(cleaned_sentence) == 0:
        return []

    # Extract the positions of all adverbs.
    # We pass the set of common adverbs to the extraction function.
    adverb_positions = _extract_adverb_positions(cleaned_sentence, COMMON_ADVERBS)

    # Return the list of adverb positions.
    return adverb_positions