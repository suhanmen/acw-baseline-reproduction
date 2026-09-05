def remove_lowercase(input_string: str) -> str:
    """
    Removes all lowercase substrings from the given input string.

    A 'lowercase substring' in this context refers to any sequence of characters
    that are exclusively lowercase letters. When such a sequence is found, it is
    removed from the original string. If the string contains a mix of uppercase
    letters and lowercase sequences, only the lowercase sequences are stripped.

    This function processes the string character by character. If it encounters
    an uppercase letter, it is kept. If it encounters a lowercase letter, it 
    initiates a sequence collection. Once a sequence of lowercase letters ends
    (either by hitting an uppercase letter or the end of the string), that entire
    sequence is discarded. Any non-letter characters (if they were to exist in the
    input based on broader interpretations, though the problem implies alphabetic
    strings) would break lowercase sequences. However, based strictly on the 
    provided examples and the term 'lowercase substrings', we treat any character 
    that is not a lowercase letter as a delimiter that stops a lowercase sequence.

    Parameters:
    input_string (str): The string from which lowercase substrings should be removed.

    Returns:
    str: The resulting string with all contiguous lowercase letter sequences removed.

    Raises:
    TypeError: If the input is not a string.
    ValueError: If the input string is not a string type (handled via TypeError check, 
                but conceptually ensures strict typing).

    Edge Cases Handled:
    - Empty string: Returns an empty string.
    - Single element: Checks if it's lowercase and returns empty string or the char itself.
    - All-equal elements: Removes all if they are lowercase.
    - Boundary values: Handles start and end of string correctly.
    - Zero length: Handled by empty string check.
    - Negative numbers: Not applicable for string input, but non-string types raise TypeError.
    """

    # Input validation
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")

    if len(input_string) == 0:
        return ""

    result = []
    current_lowercase_sequence_start_index = None

    for index, character in enumerate(input_string):
        # Check if the current character is a lowercase letter
        is_lowercase_char = character.islower() and character.isalpha()

        # Determine if we are currently inside a lowercase sequence
        is_inside_lowercase_sequence = (current_lowercase_sequence_start_index is not None)

        if is_lowercase_char:
            # If this is the start of a lowercase sequence
            if not is_inside_lowercase_sequence:
                current_lowercase_sequence_start_index = index
            # If we are inside a sequence, just continue collecting (effectively skipping)
            # because we will handle the removal when the sequence ends.
        else:
            # The character is NOT a lowercase letter (e.g., uppercase, digit, symbol, space)

            # If we were previously inside a lowercase sequence, we need to finalize the removal
            if is_inside_lowercase_sequence:
                # The sequence from start_index to current index (exclusive) is skipped.
                # We do not add the current character (index) to the result yet, 
                # but we mark that the sequence has ended.
                # Actually, the loop logic below handles adding non-start characters differently.
                # Let's restructure the logic slightly for clarity:
                # We iterate. If we are in a lowercase sequence, we skip adding to result.
                # If we encounter a non-lowercase while in a sequence, the sequence ends.
                pass

            # Determine if the current character (non-lowercase) should be added.
            # Since we are iterating through the string, if we hit a non-lowercase char:
            # 1. If we were building a lowercase sequence, that sequence is dropped. We do NOT add the sequence.
            # 2. The current character (non-lowercase) SHOULD be added to the result.

            # Reset the flag
            current_lowercase_sequence_start_index = None

            # Add the current character to the result
            result.append(character)

    # After the loop, check if there is a pending lowercase sequence at the end of the string
    if current_lowercase_sequence_start_index is not None:
        # A lowercase sequence reached the end of the string.
        # We must discard it. We do not add anything more to the result.
        pass
    else:
        # No pending sequence, or the last characters were handled (non-lowercase added above).
        # If the loop finished and we were NOT in a sequence, it means the last characters 
        # were either non-lowercase (added in the loop) or the string was empty.
        pass

    return "".join(result)

# Re-implementing with a more explicit, step-by-step state machine approach to satisfy 
# the "spell out steps" and "explicit control flow" requirements more robustly.
# The previous loop was slightly compact. Let's provide a version that explicitly 
# tracks state transitions without relying on `if/else` inside the loop for the main logic flow,
# but rather uses explicit state handling or a clearer accumulation pattern.

def remove_lowercase_v2(input_string: str) -> str:
    """
    Alternative implementation using explicit state management for maximum clarity.
    """

    # Input validation
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")

    # Handle empty input explicitly
    if len(input_string) == 0:
        return ""

    final_output_list = []

    # State variable: Is the parser currently reading a lowercase sequence?
    parsing_lowercase_sequence = False

    for character in input_string:
        # Step 1: Identify the nature of the current character
        is_current_char_lowercase = (
            character.islower() and 
            character.isalpha()
        )

        # Step 2: Decision logic based on state and character type

        if parsing_lowercase_sequence:
            # We are currently inside a lowercase sequence.
            if is_current_char_lowercase:
                # Continue the sequence. Do nothing (skip character).
                pass
            else:
                # We encountered a non-lowercase character while in a sequence.
                # The sequence ends here. The current character is a delimiter.
                # Add the current delimiter to the output.
                final_output_list.append(character)
                # Mark that we are no longer in a sequence
                parsing_lowercase_sequence = False
        else:
            # We are not currently inside a lowercase sequence.
            if is_current_char_lowercase:
                # Start of a new lowercase sequence.
                # Mark state. Do not add character to output yet.
                parsing_lowercase_sequence = True
            else:
                # Current character is NOT lowercase (and we are not in a sequence).
                # It is a standalone character (e.g., uppercase, digit).
                # Add it to the output.
                final_output_list.append(character)

    # Step 3: Post-loop cleanup
    # If the loop finished and we were still parsing a lowercase sequence,
    # it means the string ended with a lowercase sequence.
    # According to the requirement, we remove lowercase substrings.
    # So we discard the remaining sequence and add nothing more.
    if parsing_lowercase_sequence:
        pass # Do nothing, sequence is dropped
    else:
        # If not in a sequence, the last character (if any) was already added in the loop.
        # Or the string was empty (handled at start).
        pass

    # Step 4: Construct and return the final string
    return "".join(final_output_list)