def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    # Step 1: Define the set of vowels to be removed, including both lowercase and uppercase.
    VOWELS_LOWER = frozenset(['a', 'e', 'i', 'o', 'u'])
    VOWELS_UPPER = frozenset(['A', 'E', 'I', 'O', 'U'])

    # Step 2: Combine the sets of vowels into a single lookup collection.
    ALL_VOWELS = VOWELS_LOWER.union(VOWELS_UPPER)

    # Step 3: Define a helper function to check if a single character is a vowel.
    def _is_vowel(char_value):
        # Check if the character is a string and exists in our set of all vowels.
        if isinstance(char_value, str) and len(char_value) == 1:
            return char_value in ALL_VOWELS
        return False

    # Step 4: Validate the input type. The problem implies text should be a string.
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    # Step 5: Define a helper function to build the result string safely.
    # This accumulates characters that are not vowels.
    def _build_result(char_list, accumulated_chars):
        # Start with an empty list to hold the new characters.
        current_buffer = []

        # Iterate over each character in the provided list.
        for char_item in char_list:
            # Check if the character is a vowel.
            if _is_vowel(char_item):
                # Skip vowels.
                continue

            # Append non-vowel characters to the buffer.
            current_buffer.append(char_item)

        # Join the buffer into a final string and append to the accumulated result.
        new_segment = "".join(current_buffer)
        accumulated_chars.append(new_segment)
        return accumulated_chars

    # Step 6: Process the input string.
    # Initialize a list to hold segments of the result (handling potential future splits, 
    # though here we build one continuous string).
    result_segments = []

    # Convert input string to a list of characters for explicit iteration.
    char_iterator = list(text)

    # Iterate through each character to check against vowels.
    for current_char in char_iterator:
        is_vowel_flag = _is_vowel(current_char)

        if is_vowel_flag:
            # Silently ignore vowels.
            continue

        # Append non-vowel characters to the current segment being built.
        # We use a list to build the string for mutability and then join at the end.
        result_segments.append(current_char)

    # Step 7: Join the collected characters to form the final output string.
    final_output = "".join(result_segments)

    # Return the processed string.
    return final_output