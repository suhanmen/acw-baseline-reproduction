from typing import List

def remove_dirty_chars(first_string: str, second_string: str) -> str:
    """
    Removes all characters from 'first_string' that are present in 'second_string'.

    Args:
        first_string (str): The source string to filter.
        second_string (str): The string containing characters to be removed.

    Returns:
        str: The filtered string.

    Raises:
        TypeError: If inputs are not strings.
    """
    # Input Validation: Ensure both arguments are strings
    if not isinstance(first_string, str):
        raise TypeError(f"Expected string for first_string, got {type(first_string).__name__}")
    if not isinstance(second_string, str):
        raise TypeError(f"Expected string for second_string, got {type(second_string).__name__}")

    # Handle edge cases: Empty strings
    if not first_string:
        return ""
    if not second_string:
        return first_string

    # Create a set of characters to remove.
    # Using a set provides O(1) average time complexity for lookups.
    chars_to_remove = set()
    for char in second_string:
        chars_to_remove.add(char)

    # Build the resulting string by iterating through the first string.
    # We use a list to accumulate characters because string concatenation
    # in a loop is inefficient in many Python implementations.
    result_chars: List[str] = []

    for current_char in first_string:
        # Check if the character from the first string exists in the removal set
        is_dirty = current_char in chars_to_remove

        if not is_dirty:
            # If the character is "clean", add it to our result list
            result_chars.append(current_char)

    # Join the list into a final string
    final_result = "".join(result_chars)

    return final_result

if __name__ == "__main__":
    # Verification of provided assertions
    assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'