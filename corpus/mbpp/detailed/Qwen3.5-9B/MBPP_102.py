def validate_input(input_string):
    """
    Validates that the input is a string and is not empty.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input string is empty.
    """
    if not isinstance(input_string, str):
        raise TypeError(f"Expected a string, got {type(input_string).__name__}")

    if len(input_string) == 0:
        raise ValueError("Input string cannot be empty.")

    return True

def split_into_words(snake_case_string):
    """
    Splits a snake_case string into a list of individual words.

    Args:
        snake_case_string (str): The input string in snake_case format.

    Returns:
        list[str]: A list of words extracted from the input string.
    """
    words = snake_case_string.split('_')
    return words

def capitalize_word(word):
    """
    Capitalizes the first letter of a word and ensures the rest are lowercase.
    This handles potential edge cases where words might have mixed casing initially.

    Args:
        word (str): The word to be capitalized.

    Returns:
        str: The capitalized word.
    """
    if len(word) == 0:
        return word

    first_char = word[0].upper()
    remaining_chars = word[1:].lower()

    return first_char + remaining_chars

def convert_to_camel_case(snake_case_string):
    """
    Converts a snake_case string to a camelCase string.

    Logic:
    1. Split the string by underscores.
    2. Capitalize the first word (this becomes the first part of the camelCase).
    3. Capitalize the first letter of all subsequent words.
    4. Concatenate all parts together.

    Args:
        snake_case_string (str): The input string in snake_case format.

    Returns:
        str: The converted string in camelCase format.

    Raises:
        TypeError: If input is not a string.
        ValueError: If input is empty.
    """
    # Step 1: Validate the input
    validate_input(snake_case_string)

    # Step 2: Split the string into words based on the underscore delimiter
    word_list = split_into_words(snake_case_string)

    # Step 3: Ensure we don't process empty lists resulting from split (though validation prevents empty input)
    # However, if the string starts or ends with underscores (e.g., "_foo" or "foo_"), 
    # split might produce empty strings in the list. We should filter those out to be safe and robust.
    # Standard snake_case usually doesn't have leading/trailing underscores for this specific conversion logic,
    # but defensive programming suggests handling it.
    filtered_words = [w for w in word_list if len(w) > 0]

    # Step 4: Check if the list is now empty after filtering (edge case like "---")
    if len(filtered_words) == 0:
        # If input was just underscores, return an empty string or handle as error?
        # Based on assertions, we assume valid snake_case without leading/trailing underscores or consecutive underscores.
        # If it happens, returning empty string is a reasonable degenerate case behavior.
        return ""

    # Step 5: Process the first word
    first_word_capitalized = capitalize_word(filtered_words[0])

    # Step 6: Process the remaining words
    remaining_words = filtered_words[1:]
    capitalized_remaining = []

    for i in range(0, len(remaining_words)):
        current_word = remaining_words[i]
        capitalized_word = capitalize_word(current_word)
        capitalized_remaining.append(capitalized_word)

    # Step 7: Combine all parts
    result = first_word_capitalized

    for capitalized_part in capitalized_remaining:
        result = result + capitalized_part

    return result

# Export the main function name as expected by the problem statement
snake_to_camel = convert_to_camel_case