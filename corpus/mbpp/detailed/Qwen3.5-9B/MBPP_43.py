import re
from typing import Optional

def _is_valid_text(text: object) -> bool:
    """
    Validates that the input is a string.

    This function ensures that the input provided to the main function
    is of the expected type (str). If it is not, it returns False to
    indicate an invalid input.

    Args:
        text: The input value to validate.

    Returns:
        bool: True if the input is a string, False otherwise.
    """
    return isinstance(text, str)

def _extract_matching_sequences(text: str) -> list[str]:
    """
    Extracts all sequences of lowercase letters joined with an underscore.

    This function uses a regular expression to find all occurrences of the
    specific pattern within the input text. The pattern looks for one or more
    lowercase letters optionally followed by an underscore and more lowercase letters.
    However, based on the problem context and typical regex tasks, it likely aims
    to find the entire contiguous block of lowercase letters and underscores.

    Given the examples:
    - "aab_cbbbc" -> Matches the whole string because it is all lowercase letters and underscores.
    - "aab_Abbbc" -> Does not match because of the uppercase 'A'.

    Let's assume the requirement is to match a sequence consisting ONLY of 
    lowercase letters ('a'-'z') and underscores ('_'), where at least one letter 
    must be present, and underscores can appear between letters but not at the 
    very start or end of the sequence, and not consecutively (though the problem 
    statement is slightly ambiguous on strict underscore rules, we will use a 
    pattern that allows letters and underscores freely as long as no uppercase 
    or other characters are present in the contiguous sequence).

    Refined Interpretation: The problem asks for "sequences of lowercase letters 
    joined with an underscore". This implies the entire sequence must be composed 
    of [a-z_]+. However, to be safe against isolated underscores or starting/ending 
    underscores which might not be "letters joined", a more strict pattern like 
    [a-z]+(?:_[a-z]+)* is often used. But looking at the test case "aab_cbbbc", 
    it matches. If the input was "a_b_c", it should match. If "a__b" is ambiguous,
    we will stick to the most inclusive interpretation for "letters joined by underscore"
    which effectively means a token containing only lowercase letters and underscores.

    Let's use: [a-z_]+
    But wait, the test case "aab_Abbbc" returns 'Not matched!'. The regex must be case-sensitive 
    and reject uppercase.

    Let's try to find the longest contiguous substring that consists solely of lowercase 
    letters and underscores.

    Args:
        text: The input string to search within.

    Returns:
        list[str]: A list of all matched sequences found in the text.
    """
    # Compile the regex pattern.
    # Pattern explanation:
    # [a-z_] : Matches any lowercase letter or underscore.
    # +       : Matches one or more of the preceding token.
    # This ensures we capture sequences that might be purely letters or letters interspersed with underscores.
    pattern = r"[a-z_]+"

    # Find all non-overlapping matches of the pattern in the text.
    matches = re.findall(pattern, text)

    return matches

def text_match(text: object) -> str:
    """
    Finds sequences of lowercase letters joined with an underscore using regex.

    This function validates the input, searches for the specific pattern of 
    lowercase letters and underscores, and returns a predefined string indicating 
    success or failure based on whether any matches were found.

    The logic follows these steps:
    1. Validate the input is a string.
    2. If invalid, implicitly treat as no match (based on defensive programming 
       principles, though the return type suggests a binary outcome).
    3. Search for the pattern.
    4. Return 'Found a match!' if any sequence is found, otherwise 'Not matched!'.

    Args:
        text: The input string to analyze.

    Returns:
        str: 'Found a match!' if sequences matching the criteria exist, 
             'Not matched!' otherwise.

    Edge Cases Handled:
    - None or non-string input: Treated as no match.
    - Empty string: Returns 'Not matched!'.
    - String with no lowercase/underscore characters: Returns 'Not matched!'.
    - String with only uppercase characters: Returns 'Not matched!'.
    - String with numbers or symbols: Returns 'Not matched!' unless mixed with lowercase/underscore.
    """

    # Step 1: Input Validation
    if not _is_valid_text(text):
        # If the input is not a string, we cannot process it.
        # We treat this as a case where no valid match can be found.
        return "Not matched!"

    # Step 2: Extract sequences using the helper function
    matching_sequences = _extract_matching_sequences(text)

    # Step 3: Determine the result based on whether any matches were found
    if len(matching_sequences) > 0:
        return "Found a match!"
    else:
        return "Not matched!"