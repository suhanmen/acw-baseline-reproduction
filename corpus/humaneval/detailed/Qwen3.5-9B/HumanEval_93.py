from typing import Union

def _is_vowel(character: str) -> bool:
    """
    Helper function to check if a character is a vowel.
    Considers both lowercase and uppercase vowels.
    """
    if not isinstance(character, str) or len(character) != 1:
        return False
    return character.lower() in 'aeiou'

def _shift_vowel(character: str) -> str:
    """
    Helper function to shift a vowel 2 places forward in the alphabet.
    Wraps around if necessary (e.g., 'y' -> 'a', 'u' -> 'w', etc.).
    Assumes input is already validated as a vowel.
    """
    if not isinstance(character, str) or len(character) != 1:
        raise ValueError("Input to shift_vowel must be a single character string")

    if character.isupper():
        base = ord('A')
        char_code = ord(character)
    else:
        base = ord('a')
        char_code = ord(character)

    # Calculate offset from base (0-25)
    offset = char_code - base

    # Shift by 2 and handle wrap-around using modulo 26
    new_offset = (offset + 2) % 26

    # Calculate new character code and convert back to char
    new_char_code = base + new_offset

    return chr(new_char_code)

def encode(message: Union[str, None]) -> str:
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 

    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    # Validate input type explicitly
    if message is None:
        raise ValueError("Input message cannot be None")

    if not isinstance(message, str):
        raise TypeError(f"Input must be a string, received {type(message).__name__}")

    # Handle empty string edge case explicitly
    if len(message) == 0:
        return ""

    encoded_parts = []

    # Iterate through each character in the message
    for index, char in enumerate(message):
        # Explicitly check if character is empty string (defensive, though enumerate shouldn't yield empty)
        if not char:
            # If we encounter an empty character (should not happen in standard str iteration),
            # skip or raise depending on policy. Here we raise to fail fast on invalid iteration data.
            raise ValueError("Invalid character encountered: empty string found")

        # Validate that the character is a letter (ASCII or Unicode) as per problem hint "Assume only letters"
        # However, robust code should handle non-letters if they appear despite the assumption.
        # The problem statement says "Assume only letters", but defensive code validates.
        if not char.isalpha():
            # Depending on strictness, we could skip, raise, or leave as is.
            # Given "Assume only letters", encountering a non-letter is a contract violation.
            # We will treat non-letters as invalid input for this specific encoding logic
            # which is defined only for letters. We raise an error to be explicit.
            raise ValueError(f"Non-letter character found at index {index}: '{char}'. Input assumed to contain only letters.")

        # Step 1: Check if the character is a vowel
        is_vowel_flag = _is_vowel(char)

        processed_char = char

        # Step 2: If it is a vowel, shift it 2 places ahead
        if is_vowel_flag:
            processed_char = _shift_vowel(char)

        # Step 3: Swap the case of the character (either original or shifted)
        # If it was upper, make it lower. If it was lower, make it upper.
        if processed_char.isupper():
            swapped_char = processed_char.lower()
        elif processed_char.islower():
            swapped_char = processed_char.upper()
        else:
            # This branch should theoretically never be reached due to 'isalpha' check
            # and the fact that _shift_vowel preserves case before we swap.
            # If reached, it implies an edge case where case was lost or ambiguous.
            # We keep it as is to avoid infinite loops or errors, though strict logic suggests re-raise.
            swapped_char = processed_char

        # Append the processed character to our list of parts
        encoded_parts.append(swapped_char)

    # Join all parts to form the final encoded string
    return "".join(encoded_parts)