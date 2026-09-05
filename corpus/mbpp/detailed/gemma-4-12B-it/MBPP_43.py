import re
from typing import List

def text_match(text: str) -> str:
    """
    Identifies if a string contains a sequence of lowercase letters 
    joined by an underscore.

    The criteria are:
    1. The sequence must consist of lowercase letters.
    2. The letters must be joined by at least one underscore.
    3. Based on the provided test cases, the match must occur at the 
       beginning of the string or be a significant enough component, 
       but specifically, it validates the structure of lowercase 
       letters and underscores.

    Args:
        text (str): The input string to evaluate.

    Returns:
        str: 'Found a match!' if the pattern is satisfied, otherwise 'Not matched!'.
    """
    # --- Input Validation ---
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")

    if not text:
        return "Not matched!"

    # --- Regex Definition ---
    # Breakdown of the pattern:
    # ^         : Start of the string (based on test cases showing matches 
    #             fail if uppercase letters appear at the start or mixed)
    # [a-z]+    : One or more lowercase letters
    # _         : A literal underscore
    # [a-z]+    : One or more lowercase letters
    # Note: The test cases imply that if any uppercase character exists 
    # within the sequence or at the start, it fails.
    # The pattern [a-z]+_[a-z]+ matches a lowercase word, an underscore, 
    # and another lowercase word.

    # Based on:
    # "aab_cbbbc" -> Match
    # "aab_Abbbc" -> No match (Uppercase 'A' breaks it)
    # "Aaab_abbbc" -> No match (Uppercase 'A' breaks it)

    # We check if the string starts with a sequence of lowercase letters,
    # followed by an underscore, followed by more lowercase letters.
    # If any character before or within this sequence is uppercase, it fails.

    pattern = r"^[a-z]+_[a-z]+"

    # --- Matching Logic ---
    # We use re.match which checks for a match at the beginning of the string.
    # However, to ensure the whole context adheres to the "lowercase" rule
    # for the specific part we are looking for, we can use re.search 
    # or re.match depending on the strictness.

    # Given the assertions:
    # "aab_cbbbc" matches because it starts with [a-z]+_[a-z]+
    # "aab_Abbbc" fails because the underscore is followed by 'A' (not [a-z])
    # "Aaab_abbbc" fails because it starts with 'A' (not [a-z])

    match_object = re.match(pattern, text)

    if match_object is not None:
        # Additional check: 
        # The regex ^[a-z]+_[a-z]+ matches the start. 
        # We need to ensure that the very next character after the 
        # first underscore is indeed a lowercase letter. 
        # The regex [a-z]+_[a-z]+ already handles this by requiring 
        # at least one lowercase letter after the underscore.

        # However, if the input was "aab_Abbbc", re.match would fail 
        # because 'A' is not in [a-z].

        # We must also ensure that if there is text after the match, 
        # it doesn't invalidate the match (though the test cases 
        # don't strictly forbid trailing characters as long as the 
        # specific pattern is found).

        return "Found a match!"
    else:
        return "Not matched!"