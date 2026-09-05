from typing import Optional

def first_non_repeating_character(input_string: str) -> Optional[str]:
    """
    Finds the first non-repeated character in a given string.

    Args:
        input_string (str): The string to search.

    Returns:
        Optional[str]: The first character that appears exactly once, 
                        or None if all characters repeat or the string is empty.
    """
    # Validate input type
    if not isinstance(input_string, str):
        raise TypeError(f"Input must be a string, not {type(input_string).__name__}")

    # Handle empty string edge case
    if len(input_string) == 0:
        return None

    # Step 1: Count the occurrences of every character in the string.
    # We use a dictionary to store counts for O(1) average time complexity lookups.
    char_counts = {}

    for char in input_string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    # Step 2: Iterate through the string again to find the first character
    # whose count in our dictionary is exactly 1.
    # We iterate through the original string to preserve the order of appearance.
    for char in input_string:
        occurrence_count = char_counts.get(char)

        if occurrence_count == 1:
            # This is the first character encountered that does not repeat.
            return char

    # Step 3: If the loop completes without returning, all characters repeat.
    return None

if __name__ == "__main__":
    # These assertions verify the functionality against provided test cases.
    assert first_non_repeating_character("abcabc") == None
    assert first_non_repeating_character("abc") == "a"
    assert first_non_repeating_character("ababc") == "c"