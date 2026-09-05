import re
from typing import List, Tuple, Optional

def _identify_special_tokens(input_string: str) -> List[Tuple[str, int]]:
    """
    Identifies all sequences of spaces, commas, or dots in the input string.

    Returns a list of tuples containing:
    - The matched special character sequence (as a string)
    - The starting index of the match in the original string

    Parameters:
    input_string (str): The string to scan for special tokens.

    Returns:
    List[Tuple[str, int]]: A list of tuples with the special token string and its start index.
    """
    tokens: List[Tuple[str, int]] = []
    pattern = re.compile(r'[ ,\.]+')
    matches = pattern.finditer(input_string)

    current_index = 0
    for match in matches:
        token_string = match.group()
        start_index = match.start()

        # Ensure we don't have overlapping entries (redundant for finditer, but safe)
        if start_index > current_index:
            current_index = start_index

        tokens.append((token_string, start_index))

    return tokens

def _select_tokens_to_replace(tokens: List[Tuple[str, int]], count: int) -> List[Tuple[str, int]]:
    """
    Selects the first 'count' tokens from the list of identified special tokens.

    Parameters:
    tokens (List[Tuple[str, int]]): The list of all identified special tokens.
    count (int): The maximum number of occurrences to replace.

    Returns:
    List[Tuple[str, int]]: A subset of the original tokens list containing only those to be replaced.
    """
    if count <= 0:
        return []

    result_count = min(count, len(tokens))

    selected_tokens: List[Tuple[str, int]] = []
    for i in range(result_count):
        selected_tokens.append(tokens[i])

    return selected_tokens

def _construct_replaced_string(
    original_string: str, 
    tokens_to_replace: List[Tuple[str, int]], 
    replacement_char: str
) -> str:
    """
    Replaces the specific tokens identified in 'tokens_to_replace' with 'replacement_char'
    in the original string. The rest of the string remains unchanged.

    Parameters:
    original_string (str): The original input string.
    tokens_to_replace (List[Tuple[str, int]]): The list of (token_string, start_index) tuples to replace.
    replacement_char (str): The character (usually ':') to use for replacement.

    Returns:
    str: The new string with the specified tokens replaced.
    """
    # Create a list of characters to build the result string
    result_chars: List[str] = []
    current_index = 0
    index_to_check = 0

    # Sort tokens by start index to ensure we process them in order
    sorted_tokens = sorted(tokens_to_replace, key=lambda x: x[1])

    for token_info in sorted_tokens:
        token_str, start_index = token_info

        # Append characters from the original string up to the start of the current token
        if start_index > current_index:
            result_chars.append(original_string[current_index:start_index])

        # Replace the token with the replacement character
        result_chars.append(replacement_char)

        # Update the current tracking index to just after the token
        current_index = start_index + len(token_str)

    # Append the remainder of the string after the last processed token
    if current_index < len(original_string):
        result_chars.append(original_string[current_index:])

    return "".join(result_chars)

def replace_max_specialchar(input_string: str, max_occurrences: int) -> str:
    """
    Replaces the maximum number of n occurrences of spaces, commas, or dots with a colon.

    This function performs the following steps:
    1. Validates the input types and the count parameter.
    2. Identifies all contiguous sequences of spaces, commas, or dots in the string.
    3. Selects up to 'max_occurrences' of these sequences to replace.
    4. Constructs the new string with the selected sequences replaced by colons.

    Parameters:
    input_string (str): The string to process.
    max_occurrences (int): The maximum number of special character sequences to replace.

    Returns:
    str: The processed string with replacements made.

    Raises:
    TypeError: If input_string is not a string or max_occurrences is not an integer.
    ValueError: If max_occurrences is negative.
    """
    # Input Validation

    # Check if input_string is a string
    if not isinstance(input_string, str):
        raise TypeError(f"input_string must be a string, got {type(input_string).__name__}")

    # Check if max_occurrences is an integer (bool is a subclass of int, so check explicitly)
    if not isinstance(max_occurrences, int) or isinstance(max_occurrences, bool):
        raise TypeError(f"max_occurrences must be an integer, got {type(max_occurrences).__name__}")

    # Check for negative values
    if max_occurrences < 0:
        raise ValueError(f"max_occurrences must be non-negative, got {max_occurrences}")

    # Handle edge case: empty string or zero max occurrences
    if not input_string or max_occurrences == 0:
        return input_string

    # Step 1: Identify all special tokens (spaces, commas, dots)
    all_tokens = _identify_special_tokens(input_string)

    # Step 2: Select the tokens to replace (up to max_occurrences)
    tokens_to_replace = _select_tokens_to_replace(all_tokens, max_occurrences)

    # Step 3: Construct the final string with replacements
    final_string = _construct_replaced_string(input_string, tokens_to_replace, ':')

    return final_string