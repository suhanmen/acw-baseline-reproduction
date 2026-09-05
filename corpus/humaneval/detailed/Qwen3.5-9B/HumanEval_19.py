from typing import List, Optional


def _create_word_to_value_map() -> dict:
    """
    Creates and returns a mapping from number words ('zero' through 'nine')
    to their integer values (0 through 9).

    This function encapsulates the mapping logic so it can be imported
    or reused if necessary, and keeps the main sorting function clean.
    """
    mapping = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    return mapping


def _validate_number_token(token: str, valid_tokens: frozenset) -> Optional[int]:
    """
    Validates a single number token string.

    If the token exists in the set of valid tokens, returns its integer value.
    If the token is empty or not found in the valid set, returns None.

    Args:
        token: The string token to validate (e.g., 'three', '1').
        valid_tokens: A frozenset of acceptable number words.

    Returns:
        The integer value of the token if valid, otherwise None.
    """
    if not token:
        return None

    if token in valid_tokens:
        return token  # We will convert this to int later using a separate map to keep logic modular
    return None


def _token_to_int(token: str, word_to_value_map: dict) -> Optional[int]:
    """
    Converts a valid word token to its integer representation.

    Args:
        token: The validated word token.
        word_to_value_map: Dictionary mapping words to integers.

    Returns:
        Integer value if the token is in the map, otherwise None.
    """
    if token in word_to_value_map:
        return word_to_value_map[token]
    return None


def _split_and_filter_tokens(input_string: str) -> List[str]:
    """
    Splits the input string by whitespace and filters out empty strings.

    This handles cases where there are leading/trailing spaces or 
    multiple consecutive spaces between numbers.

    Args:
        input_string: The raw input string.

    Returns:
        A list of non-empty strings.
    """
    tokens = input_string.split()
    return tokens


def _check_all_tokens_valid(tokens: List[str], valid_tokens: frozenset) -> bool:
    """
    Checks if every token in the list is a valid number word.

    Args:
        tokens: List of number words.
        valid_tokens: Set of acceptable words.

    Returns:
        True if all tokens are valid, False otherwise.
    """
    for token in tokens:
        if token not in valid_tokens:
            return False
    return True


def _convert_tokens_to_integers(tokens: List[str], word_to_value_map: dict) -> List[int]:
    """
    Converts a list of valid word tokens to a list of integers.

    Args:
        tokens: List of valid word tokens.
        word_to_value_map: Mapping from words to integers.

    Returns:
        List of integer values corresponding to the input tokens.
    """
    values = []
    for token in tokens:
        integer_value = word_to_value_map[token]
        values.append(integer_value)
    return values


def _reconstruct_output_string(sorted_values: List[int], word_to_value_map: dict) -> str:
    """
    Converts a list of sorted integers back into a space-delimited string.

    Args:
        sorted_values: List of integers to convert.
        word_to_value_map: Reverse mapping (int -> word) derived from the forward map.

    Returns:
        A space-delimited string of number words.
    """
    if not sorted_values:
        return ""

    result_tokens = []
    for value in sorted_values:
        if value in word_to_value_map:
            result_tokens.append(word_to_value_map[value])
        else:
            # This case should theoretically not be reached if validation passed,
            # but we handle it defensively by including the string representation.
            result_tokens.append(str(value))

    return " ".join(result_tokens)


def _int_to_word_converter(word_to_value_map: dict) -> dict:
    """
    Creates a reverse mapping from integer values to number words.

    Args:
        word_to_value_map: Original mapping from word to int.

    Returns:
        Dictionary mapping int to word.
    """
    inverse_map = {}
    for word, value in word_to_value_map.items():
        inverse_map[value] = word
    return inverse_map


def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of number words ('zero' through 'nine')
    in ascending order and returns the result as a space-delimited string.

    Valid choices are: 'zero', 'one', 'two', 'three', 'four', 'five', 
    'six', 'seven', 'eight', 'nine'.

    Any input containing invalid tokens, non-whitespace delimiters, 
    or unexpected formats is detected, and the behavior depends on the 
    specific invalidity. Per defensive programming principles, we raise 
    a ValueError if the input is not strictly valid according to the problem 
    description (containing only valid number words).

    If the input is empty, an empty string is returned.

    Args:
        numbers: A string containing space-separated number words.

    Returns:
        A string with the number words sorted alphabetically by their numeric value.

    Raises:
        ValueError: If the input contains any token that is not a valid number word.
        TypeError: If the input is not a string.

    Examples:
        >>> sort_numbers('three one five')
        'one three five'
        >>> sort_numbers('')
        ''
        >>> sort_numbers('nine eight seven')
        'seven eight nine'
        >>> sort_numbers('zero')
        'zero'
        >>> sort_numbers('one two three four five six seven eight nine')
        'one two three four five six seven eight nine'
        >>> sort_numbers('invalid')
        Traceback (most recent call last):
            ...
        ValueError: Invalid number token found: 'invalid'
    """
    # Define the set of valid tokens once
    valid_tokens_frozenset = frozenset([
        'zero', 'one', 'two', 'three', 'four', 'five', 
        'six', 'seven', 'eight', 'nine'
    ])

    # Step 1: Handle Type Safety
    if not isinstance(numbers, str):
        raise TypeError(f"Input must be a string, received {type(numbers).__name__}")

    # Step 2: Handle Empty Input Explicitly
    if not numbers.strip():
        return ""

    # Step 3: Tokenize the input string
    tokens = _split_and_filter_tokens(numbers)

    # Step 4: Validate that no tokens are missing (all parts must be valid words)
    # We check if every token exists in our valid set.
    # If not, we identify the invalid one.
    invalid_token = None
    for token in tokens:
        if token not in valid_tokens_frozenset:
            invalid_token = token
            break

    if invalid_token is not None:
        raise ValueError(f"Invalid number token found: '{invalid_token}'")

    # Step 5: Create the mapping for conversion
    word_to_value_map = _create_word_to_value_map()

    # Step 6: Convert valid words to integers
    integer_values = _convert_tokens_to_integers(tokens, word_to_value_map)

    # Step 7: Sort the integer values
    sorted_values = sorted(integer_values)

    # Step 8: Convert sorted integers back to words
    int_to_word_map = _int_to_word_converter(word_to_value_map)
    sorted_words = _reconstruct_output_string(sorted_values, int_to_word_map)

    return sorted_words