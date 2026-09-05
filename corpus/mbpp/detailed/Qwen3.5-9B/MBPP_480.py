def _create_character_frequency_map(input_string):
    """
    Constructs a dictionary mapping each character to its occurrence count.

    Args:
        input_string (str): The string to analyze.

    Returns:
        dict: A dictionary where keys are characters and values are their counts.
              Returns an empty dictionary if the input string is empty.
    """
    frequency_map = {}

    # Explicit iteration to count occurrences
    for current_char in input_string:
        if current_char in frequency_map:
            frequency_map[current_char] += 1
        else:
            frequency_map[current_char] = 1

    return frequency_map

def _get_maximum_count(counts_dictionary):
    """
    Finds the highest occurrence count value in the frequency map.

    Args:
        counts_dictionary (dict): The dictionary of character counts.

    Returns:
        int or None: The highest count value. Returns None if the dictionary is empty.
    """
    if not counts_dictionary:
        return None

    max_count = 0
    for count in counts_dictionary.values():
        if count > max_count:
            max_count = count

    return max_count

def _find_characters_with_max_count(counts_dictionary, max_occurrence):
    """
    Identifies all characters that appear with the maximum occurrence count.
    Returns them as a sorted list to ensure deterministic ordering in case of ties.

    Args:
        counts_dictionary (dict): The dictionary of character counts.
        max_occurrence (int): The maximum count value found in the dictionary.

    Returns:
        list: A list of characters that have the max_occurrence count, sorted by character.
    """
    matching_characters = []

    # Iterate through items to find characters matching the max count
    for character, count in counts_dictionary.items():
        if count == max_occurrence:
            matching_characters.append(character)

    # Sort the list of characters (lexicographically) to handle ties consistently
    matching_characters.sort()

    return matching_characters

def _get_first_from_tied_list(character_list):
    """
    Selects the first element from a list of tied maximum characters.
    This provides a deterministic rule for tie-breaking (lexicographically first).

    Args:
        character_list (list): List of characters that share the maximum count.

    Returns:
        str or None: The first character in the sorted list, or None if the list is empty.
    """
    if not character_list:
        return None

    return character_list[0]

def get_max_occuring_char(input_string):
    """
    Finds the maximum occurring character in a given string.

    Logic steps:
    1. Handle edge case where input is None.
    2. Handle edge case where input is an empty string.
    3. Build a frequency map of all characters.
    4. Determine the maximum frequency value.
    5. If no characters exist (should be caught by step 2), return None.
    6. Identify all characters that share the maximum frequency.
    7. In case of a tie, return the character that comes first alphabetically.

    Args:
        input_string (str): The string to analyze.

    Returns:
        str or None: The character with the highest frequency. 
                     Returns None if the input is empty, None, or invalid.
    """
    # Validate input type explicitly
    if not isinstance(input_string, str):
        return None

    # Handle empty input explicitly
    if len(input_string) == 0:
        return None

    # Step 1: Create frequency map
    frequency_map = _create_character_frequency_map(input_string)

    # Step 2: Determine maximum count
    max_count = _get_maximum_count(frequency_map)

    # Theoretically max_count should not be None here if input was non-empty,
    # but we check defensively.
    if max_count is None:
        return None

    # Step 3: Find all characters with the maximum count
    max_count_characters = _find_characters_with_max_count(frequency_map, max_count)

    # Step 4: Resolve ties by selecting the first one (lexicographically)
    result_character = _get_first_from_tied_list(max_count_characters)

    return result_character