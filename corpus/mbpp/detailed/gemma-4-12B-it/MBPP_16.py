import re
from typing import List

def text_lowercase_underscore(text: str) -> str:
    """
    Identifies if a string contains a sequence of lowercase letters 
    joined by an underscore, where both parts are lowercase letters.

    The function follows these rules:
    1. Input must be a string.
    2. The pattern looks for: 
       - A sequence of lowercase letters [a-z]+
       - Followed by an underscore '_'
       - Followed by another sequence of lowercase letters [a-z]+
    3. If the string contains any uppercase letters in the sequences,
       it does not count as a match for this specific logic.
    4. Based on the provided assertions:
       - "aab_cbbbc" -> 'Found a match!'
       - "aab_Abbbc" -> 'Not matched!' (Contains uppercase 'A')
       - "Aaab_abbbc" -> 'Not matched!' (Contains uppercase 'A')

    Args:
        text (str): The input string to evaluate.

    Returns:
        str: 'Found a match!' if valid sequence is found, else 'Not matched!'
    """
    # 1. Input Validation
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")

    # 2. Handle Empty Input
    if not text:
        return "Not matched!"

    # 3. Define the Logic
    # The requirement implies we are looking for a specific pattern:
    # lowercase_letters + underscore + lowercase_letters
    # However, the presence of ANY uppercase letters in the sequence
    # (or potentially the whole string, based on assertions) invalidates the match.

    # Let's first check if there are any uppercase letters anywhere.
    # The assertions "aab_Abbbc" and "Aaab_abbbc" result in "Not matched!".
    # This suggests that the existence of an uppercase letter anywhere 
    # in the sequence/string disqualifies it.

    has_uppercase = False
    for char in text:
        if char.isupper():
            has_uppercase = True
            break

    if has_uppercase:
        return "Not matched!"

    # 4. Regex Pattern Matching
    # Pattern: One or more lowercase letters, an underscore, one or more lowercase letters.
    # We use \b or start/end anchors or simply search for the pattern.
    # Based on the assertions, we are looking for the pattern within the text.

    # Pattern explanation:
    # [a-z]+    : One or more lowercase letters
    # _         : A literal underscore
    # [a-z]+    : One or more lowercase letters
    pattern = r"[a-z]+_[a-z]+"

    # We use re.search to see if this pattern exists anywhere in the string.
    match_object = re.search(pattern, text)

    if match_object is not None:
        return "Found a match!"
    else:
        return "Not matched!"

# The following assertions are provided to ensure the function behaves correctly.
if __name__ == "__main__":
    # These are the required assertions from the problem description.
    assert text_lowercase_underscore("aab_cbbbc") == 'Found a match!'
    assert text_lowercase_underscore("aab_Abbbc") == 'Not matched!'
    assert text_lowercase_underscore("Aaab_abbbc") == 'Not matched!'