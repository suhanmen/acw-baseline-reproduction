from typing import List, Union


def validate_n(n: Union[int, float, str, object]) -> int:
    """
    Validates and converts the threshold value 'n'.

    The problem implies 'n' should be a non-negative integer representing a word length.
    If 'n' is zero or negative, filtering for "longer than n" will include words 
    with length 1, 2, 3, etc. However, logically, a length threshold for words 
    is typically expected to be a non-negative integer.

    This function raises a ValueError if the input is invalid.
    """
    if not isinstance(n, int):
        raise TypeError(f"The threshold 'n' must be an integer. Received type: {type(n).__name__}")

    # While negative numbers are technically integers, a word length filter 
    # less than zero doesn't make practical sense in standard contexts (all words are > -5).
    # However, strict adherence to "longer than n" allows negatives. 
    # We will accept non-negative integers as the robust standard, or strictly integers.
    # Given the examples (3, 2, 5), positive integers are expected.
    # Let's enforce non-negative to prevent logical oddities, though mathematically > -100 works.
    # To be safe and standard, we accept any integer but note that the logic holds.
    # For strict production quality, we might enforce n >= 0, but the prompt doesn't explicitly ban negatives.
    # Let's stick to the core requirement: it must be an integer.

    if n < 0:
        raise ValueError(f"The threshold 'n' must be non-negative. Received: {n}")

    return n


def validate_word_list(words: Union[str, List[str], object]) -> List[str]:
    """
    Validates and normalizes the input list of words.

    Handles the case where a string is passed instead of a list, which is 
    a common edge case in competitive programming or loose typing scenarios.
    If a string is passed, it is treated as a sequence of characters (each char is a "word"),
    OR we check if the intent is to pass a string representing multiple words.

    Looking at the problem: `long_words(3,"python is a programming language")`
    The second argument is a string: "python is a programming language".
    The expected output treats spaces as delimiters.
    So, if the input is a string, we must split it by whitespace.
    If the input is a list, we return it as is.
    """
    if isinstance(words, str):
        # Split the string by whitespace to get individual words
        # This handles multiple spaces gracefully via split() default behavior
        result = words.split()
    elif isinstance(words, list):
        # Ensure all elements in the list are strings
        validated_items = []
        for item in words:
            if not isinstance(item, str):
                raise TypeError(f"All items in the word list must be strings. Found: {type(item).__name__}")
            validated_items.append(item)
        result = validated_items
    else:
        raise TypeError(f"The input must be a string or a list of strings. Received type: {type(words).__name__}")

    return result


def extract_long_words(words: List[str], threshold: int) -> List[str]:
    """
    Core logic to filter words based on length.

    Args:
        words: List of strings to filter.
        threshold: The integer n. Words must be strictly longer than this.

    Returns:
        A new list containing only the words that are longer than 'threshold'.
    """
    result = []

    for current_word in words:
        current_word_length = len(current_word)

        if current_word_length > threshold:
            result.append(current_word)

    return result


def long_words(n: Union[int, float, str, object], words: Union[str, List[str], object]) -> List[str]:
    """
    Main function to shortlist words that are longer than n from a given list of words.

    Steps:
    1. Validate and normalize the threshold 'n'.
    2. Validate and normalize the input 'words'.
    3. Filter the list based on the threshold.
    4. Return the filtered list.
    """
    # Step 1: Validate 'n'
    validated_threshold = validate_n(n)

    # Step 2: Validate and process 'words'
    validated_word_list = validate_word_list(words)

    # Step 3: Extract long words
    final_result = extract_long_words(validated_word_list, validated_threshold)

    return final_result