def text_lowercase_underscore(text):
    """
    Finds sequences of lowercase letters joined with an underscore in the given text.
    Returns 'Found a match!' if such sequences exist, and 'Not matched!' otherwise.

    Args:
        text: The input string to be checked.

    Returns:
        'Found a match!' if sequences are found, 'Not matched!' otherwise.
    """
    # Step 1: Check if the input is a string
    if not isinstance(text, str):
        return 'Not matched!'

    # Step 2: Check if the string contains at least one underscore
    if '_' not in text:
        return 'Not matched!'

    # Step 3: Split the string into parts using underscore as delimiter
    parts = text.split('_')

    # Step 4: Remove any empty strings from the split parts
    non_empty_parts = [part for part in parts if part]

    # Step 5: Check if each part consists only of lowercase letters
    for part in non_empty_parts:
        if not part.islower() or not part.isalpha():
            return 'Not matched!'

    # Step 6: If all checks passed, return the match found
    return 'Found a match!'