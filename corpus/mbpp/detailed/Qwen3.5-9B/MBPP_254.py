from typing import List

def _is_word(starting_with_ae: bool, char: str, is_start: bool) -> bool:
    """
    Determines if a character can be part of a word that starts with 'a' or 'e'.

    Logic:
    - If it's the start of a new word:
        - The character MUST be 'a' or 'e' for the word to qualify.
    - If it's not the start of a new word:
        - It can be any letter (part of the qualifying word).
        - If it's a non-letter, it signals the end of the current word.

    Returns:
        True if this character contributes to a potential qualifying word.
        False if this character breaks a potential qualifying word or doesn't start one.
    """
    # Check if current character is a letter
    if not char.isalpha():
        # Non-letters cannot be part of the word and signal a break
        return False

    # Check if it's the start of a word
    if is_start:
        # Only 'a' or 'e' can start a qualifying word
        if char == 'a' or char == 'e':
            return True
        else:
            # Starts with other letter, not qualifying
            return False
    else:
        # Not start, but it's a letter, so it continues the current word
        return True


def _extract_qualifying_words(input_string: str) -> List[str]:
    """
    Iterates through the input string and extracts words that start with 'a' or 'e'.

    Returns a list of strings matching the criteria.
    """
    result_words: List[str] = []
    current_word_chars: List[str] = []
    is_word_starting: bool = True  # State flag for the next character

    # Iterate over each character in the input string
    for char_index in range(len(input_string)):
        char = input_string[char_index]
        next_is_start = False

        # Determine if the current character starts a new word
        if char_index == 0 or not input_string[char_index - 1].isalpha():
            next_is_start = True

        # Check if this character contributes to a qualifying word
        is_qualifying_part = _is_word_ae(
            starting_with_ae=True, 
            char=char, 
            is_start=next_is_start
        )

        if is_qualifying_part:
            # Add character to current potential word
            current_word_chars.append(char)
        else:
            # Character does not belong to a qualifying word
            # Check if we have a completed qualifying word in current_word_chars
            if current_word_chars:
                # We had a sequence that started as qualifying but now stopped
                # Verify if the sequence was actually a full word (ended by non-alpha)
                # Since we only add when is_qualifying_part is True, 
                # and is_qualifying_part becomes False on non-alpha or bad start,
                # we need to ensure we only commit the word if it was properly formed.

                # Re-evaluate logic: 
                # If we are here, the current char broke the chain.
                # The current_word_chars holds the prefix that looked promising.
                # We must ensure the word was fully formed before this break.
                # Actually, the logic above accumulates. Let's refine the accumulation strategy.
                pass

            # Reset state for next potential word
            current_word_chars = []
            is_word_starting = next_is_start

    # Post-processing: Check if the string ended with a qualifying word
    if current_word_chars:
        # If there are characters left, we need to verify if this was a valid word.
        # Based on the logic in _is_word_ae:
        # - It starts with 'a' or 'e' (if is_start was true)
        # - It continues with letters
        # - It stops when a non-letter is encountered (which sets is_start=True for next)
        # - OR when string ends.

        # Let's reconstruct the word based on our accumulation logic.
        # The accumulation logic above accumulates ONLY if _is_word returns True.
        # So current_word_chars contains only letters that were part of a potential match.
        # We need to check if the START of this accumulated sequence was 'a' or 'e'.

        if not current_word_chars:
            current_word_chars = []
        else:
            first_char = current_word_chars[0]
            if first_char == 'a' or first_char == 'e':
                # It was a valid word
                word = "".join(current_word_chars)
                result_words.append(word)
            else:
                # It started with something else, discard
                current_word_chars = []

    return result_words


def words_ae(input_string: str) -> List[str]:
    """
    Finds all words starting with 'a' or 'e' in a given string.

    A word is defined as a contiguous sequence of alphabetic characters.
    The function validates the input and handles edge cases explicitly.

    Args:
        input_string: The string to search within. Can contain any characters.

    Returns:
        A list of strings representing words that start with 'a' or 'e'.
        Returns an empty list if no such words exist or if input is invalid.

    Raises:
        TypeError: If input_string is not a string.
    """
    # Input Validation
    if not isinstance(input_string, str):
        raise TypeError(f"Expected string input, received {type(input_string).__name__}")

    # Handle empty input explicitly
    if len(input_string) == 0:
        return []

    # Initialize storage
    result: List[str] = []
    current_chars: List[str] = []
    at_start_of_word: bool = True

    # Process each character with explicit control flow
    char_index = 0
    string_length = len(input_string)

    while char_index < string_length:
        current_char = input_string[char_index]
        is_alpha = current_char.isalpha()

        # Determine if we are at the start of a new word
        # A new word starts at index 0 or after a non-alphabetic character
        prev_char_is_alpha = False
        if char_index > 0:
            prev_char = input_string[char_index - 1]
            prev_char_is_alpha = prev_char.isalpha()

        is_new_word_start = not prev_char_is_alpha

        # Logic to determine if current char extends a qualifying word
        # Qualifying condition:
        # 1. If at new word start: char MUST be 'a' or 'e'
        # 2. If continuing word: char MUST be a letter (non-letter breaks the word)

        if is_new_word_start:
            if current_char == 'a' or current_char == 'e':
                # Start of a qualifying word
                current_chars.append(current_char)
                at_start_of_word = False
            else:
                # Starts with non-ae letter, not a target word
                current_chars = []
                at_start_of_word = True
        else:
            # Continuing an existing word
            if is_alpha:
                # Continue accumulating letters
                current_chars.append(current_char)
                at_start_of_word = False
            else:
                # Non-alphabetic character encountered in the middle/end of a word
                # This signifies the end of the current word accumulation
                # Check if the accumulated word was valid
                if len(current_chars) > 0 and (current_chars[0] == 'a' or current_chars[0] == 'e'):
                    completed_word = "".join(current_chars)
                    result.append(completed_word)

                # Reset for next potential word
                current_chars = []
                at_start_of_word = True

        # Move to next character
        char_index += 1

    # Final check after loop ends (handle word ending at the very end of string)
    if len(current_chars) > 0:
        if current_chars[0] == 'a' or current_chars[0] == 'e':
            completed_word = "".join(current_chars)
            result.append(completed_word)

    return result