def _is_punctuation_character(character: str) -> bool:
    """
    Determines if a given single character is a punctuation mark.

    Accepts a string of exactly one character.
    Returns True if the character is in the set of standard ASCII punctuation,
    False otherwise.

    Raises:
        TypeError: If the input is not a string or not a single character.
    """
    if not isinstance(character, str):
        raise TypeError("Punctuation check expects a string.")

    if len(character) != 1:
        raise TypeError("Punctuation check expects a single character string.")

    standard_punctuation = {
        '.', ',', '!', '?', ';', ':', 
        '"', "'", '(', ')', '[', ']', '{', '}',
        '-', '_', ' ', '/'
    }

    return character in standard_punctuation


def _extract_ending_punctuation(remaining_text: str) -> str:
    """
    Extracts all consecutive punctuation characters from the very end of the string.

    Returns:
        A string containing only the trailing punctuation characters.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(remaining_text, str):
        raise TypeError("Text extraction expects a string input.")

    trailing_punctuation = ""
    length = len(remaining_text)

    # Iterate backwards through the string
    index = length - 1

    while index >= 0:
        current_char = remaining_text[index]
        if _is_punctuation_character(current_char):
            trailing_punctuation = current_char + trailing_punctuation
            index -= 1
        else:
            break

    return trailing_punctuation


def _strip_ending_punctuation(text: str, punctuation: str) -> str:
    """
    Removes the extracted punctuation from the end of the text.

    Args:
        text: The original string.
        punctuation: The substring to remove from the end.

    Returns:
        The text with the specific trailing punctuation removed.

    Raises:
        TypeError: If inputs are not strings.
        ValueError: If the punctuation string is not a suffix of the text.
    """
    if not isinstance(text, str):
        raise TypeError("Text strip expects a string for 'text'.")
    if not isinstance(punctuation, str):
        raise TypeError("Text strip expects a string for 'punctuation'.")

    # Check if punctuation is actually a suffix
    if not text.endswith(punctuation):
        raise ValueError("The extracted punctuation does not match the end of the text.")

    result_text = text[:-len(punctuation)]
    return result_text


def _trim_whitespace(text: str) -> str:
    """
    Removes leading and trailing whitespace from the text.

    Args:
        text: The input string.

    Returns:
        The string with leading and trailing whitespace removed.

    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Whitespace trimming expects a string input.")

    stripped_text = text.strip()
    return stripped_text


def _identify_target_word(text_with_punctuation: str) -> str:
    """
    Identifies and extracts the word that should be matched at the end.

    This function attempts to find the last sequence of alphabetic characters.
    If no alphabetic characters are found after stripping whitespace, 
    it considers the entire stripped string as the target (if it wasn't empty).

    Args:
        text_with_punctuation: The text after removing trailing punctuation.

    Returns:
        The identified word string.

    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(text_with_punctuation, str):
        raise TypeError("Word identification expects a string input.")

    # Split the text into words based on whitespace
    word_list = text_with_punctuation.split()

    if not word_list:
        # Handle case where there are no words left after splitting (e.g., "   ...")
        # In this specific logic context, we return an empty string to trigger "Not matched"
        return ""

    # Get the last word from the list
    target_word = word_list[-1]

    return target_word


def text_match_word(input_string: str) -> str:
    """
    Matches a word at the end of a string, ignoring optional trailing punctuation.

    The logic follows these steps:
    1. Validate that input is a string.
    2. Strip leading/trailing whitespace.
    3. Check if the string is empty after trimming.
    4. Extract trailing punctuation characters from the end.
    5. Remove the trailing punctuation to get the core text.
    6. Identify the target word (last word) from the core text.
    7. Check if the original stripped text (minus trailing punctuation) 
       ends with the target word.

    Returns:
        'Found a match!' if the target word is at the end, otherwise 'Not matched!'.

    Raises:
        TypeError: If the input is not a string.
    """
    # Step 0: Input Validation
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")

    # Step 1: Handle empty string or whitespace-only string early
    if input_string.strip() == "":
        return "Not matched!"

    # Step 2: Remove leading and trailing whitespace
    clean_text = _trim_whitespace(input_string)

    # Step 3: Extract punctuation from the very end
    extracted_punctuation = _extract_ending_punctuation(clean_text)

    # Step 4: Remove the extracted punctuation from the text
    core_text = _strip_ending_punctuation(clean_text, extracted_punctuation)

    # Step 5: Identify the target word
    target_word = _identify_target_word(core_text)

    # Step 6: Handle case where no valid word was identified (e.g., core_text was punctuation or symbols)
    if not target_word:
        return "Not matched!"

    # Step 7: Check if the core text ends with the target word
    # Note: We compare the full core_text against the word suffix.
    # Since 'identify_target_word' takes the last word from split(), 
    # we just need to ensure core_text ends with that word.

    ends_with_match = False

    if core_text == target_word:
        # Exact match case (e.g., input "hello" -> core "hello", word "hello")
        ends_with_match = True
    else:
        # Check if core_text ends with the specific word string
        ends_with_match = core_text.endswith(target_word)

    if ends_with_match:
        return "Found a match!"
    else:
        return "Not matched!"