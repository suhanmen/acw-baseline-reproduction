from typing import Tuple, Union

def _is_lowercase_word(text: str) -> bool:
    """
    Helper function to determine if the input string represents a valid sequence.

    A valid sequence is defined as:
    1. Being non-empty.
    2. Consisting only of lowercase alphabetic characters ('a'-'z').
    3. Joined with single underscores ('_').
    4. Starting and ending with a lowercase letter (no leading or trailing underscores).

    Args:
        text (str): The string to validate.

    Returns:
        bool: True if the string is a valid lowercase word sequence, False otherwise.
    """
    if not text:
        return False

    # Check for leading or trailing underscores
    if text.startswith('_') or text.endswith('_'):
        return False

    length = len(text)
    i = 0

    while i < length:
        char = text[i]

        if char == '_':
            # If we encounter an underscore, ensure there is a character immediately following it
            if i + 1 >= length:
                return False
            # Ensure the next character is an underscore, which would be invalid (multiple underscores)
            # Actually, multiple underscores are allowed between words, but let's stick to the core logic:
            # The problem implies a sequence like "word1_word2". 
            # Let's re-evaluate: "aab_cbbbc" is valid. 
            # Does "aab__cbbbc" (double underscore) count? Usually no for "sequence of words joined".
            # Standard interpretation: single underscore separators.
            if text[i+1] == '_':
                return False

            # Move to the next character
            i += 1
        elif 'a' <= char <= 'z':
            i += 1
        else:
            # Invalid character found (e.g., uppercase, number, special char)
            return False

    return True

def _extract_lowercase_sequences(text: str) -> Union[Tuple[str, ...], Tuple[None, None]]:
    """
    Extracts all valid lowercase underscore-separated sequences from the input text.

    Args:
        text (str): The input text to search within.

    Returns:
        tuple: A tuple of valid sequences found, or (None, None) if none found.
    """
    sequences = []
    text_length = len(text)
    i = 0

    while i < text_length:
        char = text[i]

        if char == '_':
            # Skip underscores, they act as delimiters
            i += 1
            continue

        # Start of a potential word
        start_index = i
        is_valid_segment = True

        while i < text_length:
            current_char = text[i]

            if current_char == '_':
                # End of the current word segment
                break
            elif 'a' <= current_char <= 'z':
                i += 1
            else:
                # Invalid character breaks the sequence
                is_valid_segment = False
                break

        # Check if we found a valid segment
        if i > start_index and is_valid_segment:
            extracted_word = text[start_index:i]
            if _is_lowercase_word(extracted_word):
                sequences.append(extracted_word)

        i += 1

    return tuple(sequences)

def text_lowercase_underscore(input_text: str) -> str:
    """
    Function to find sequences of lowercase letters joined with an underscore.

    Logic:
    1. Validates that the input is a string.
    2. Searches for segments within the text that match the criteria:
       - Non-empty
       - Contains only lowercase letters and single underscores as separators
       - No leading/trailing underscores
    3. If exactly one such sequence is found, returns 'Found a match!'.
    3. If zero or more than one such sequence is found, returns 'Not matched!'.

    Note: Based on the assertions provided:
    - "aab_cbbbc" (one valid word) -> 'Found a match!'
    - "aab_Abbbc" (contains uppercase, so the part "aab" is valid but "Abbbc" is not; 
      actually, the whole string isn't a single valid sequence if we consider the whole string.
      However, the logic implies we are looking for the entire input to BE a valid sequence,
      OR we are looking if ANY valid sequence exists?

      Let's re-read the assertions carefully.
      Input: "aab_cbbbc" -> Found.
      Input: "aab_Abbbc" -> Not matched. Here "aab" is valid, "Abbbc" is not. 
      Input: "Aaab_abbbc" -> Not matched. Here "Aaab" is not, "abbbc" is.

      Hypothesis 1: The function checks if the ENTIRE INPUT string is a valid sequence.
      - "aab_cbbbc": Valid? Yes.
      - "aab_Abbbc": Valid? No, because of 'A'.
      - "Aaab_abbbc": Valid? No, because of 'A' at start.

      Hypothesis 2: The function checks if there is EXACTLY ONE contiguous valid sequence 
      that covers the whole relevant part of the string (ignoring garbage at ends)?
      Unlikely given the simplicity.

      Hypothesis 3: The function checks if the input string is a valid sequence of lowercase 
      words joined by underscores. If the string contains ANY invalid character (uppercase, digit, etc), 
      or has invalid structure, it returns 'Not matched!'.

      Let's test Hypothesis 1 against "aab_cbbbc".
      Is "aab_cbbbc" a sequence of lowercase letters joined by underscore?
      Yes. 'a', 'a', 'b', '_', 'c', 'b', 'b', 'b', 'c'. All lower, separated by one '_'.

      "aab_Abbbc": Contains 'A'. Invalid. -> Not matched.
      "Aaab_abbbc": Contains 'A'. Invalid. -> Not matched.

      What if input is "word1_word2"? Valid -> Found.
      What if input is "word1 word2"? Invalid (space) -> Not matched.
      What if input is "_word"? Invalid (leading _) -> Not matched.

      This seems to be the most logical interpretation: 
      The function validates if the WHOLE input string conforms to the pattern.

      Pattern: One or more lowercase words, separated by single underscores, 
               with no leading/trailing underscores, and no other characters.

    Args:
        input_text (str): The string to check.

    Returns:
        str: 'Found a match!' if the entire string is a valid sequence, 
             'Not matched!' otherwise.
    """

    # Input Validation
    if not isinstance(input_text, str):
        raise TypeError("Input must be a string.")

    # According to the logic derived from assertions:
    # The function likely expects the entire input to be a valid sequence.
    # Let's implement the check for the entire string.

    if _is_lowercase_word(input_text):
        return 'Found a match!'
    else:
        return 'Not matched!'