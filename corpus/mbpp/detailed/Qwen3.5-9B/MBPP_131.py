from typing import List, Tuple

# Define the set of valid vowels to check against.
# We include both lowercase and uppercase variants for comprehensive coverage.
VALID_VOWELS: set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}


def _identify_vowel_indices(s: str) -> List[int]:
    """
    Iterates through the input string and identifies the zero-based indices
    of all characters that are vowels.

    Args:
        s (str): The input string to analyze.

    Returns:
        List[int]: A list of integers representing the indices of vowels in the string.
                   Returns an empty list if no vowels are found.
    """
    indices: List[int] = []

    # Iterate over the string using enumerate to get both index and character.
    for index, character in enumerate(s):
        # Explicitly check if the current character exists in our set of valid vowels.
        if character in VALID_VOWELS:
            # If it is a vowel, append the current index to our list.
            indices.append(index)

    # Return the collected list of indices.
    return indices


def _extract_vowels(s: str, indices: List[int]) -> List[str]:
    """
    Extracts the actual vowel characters from the input string based on the
    previously identified indices.

    Args:
        s (str): The original input string.
        indices (List[int]): The list of indices corresponding to vowels.

    Returns:
        List[str]: A list of vowel characters in their original order.
    """
    vowels: List[str] = []

    # Iterate through the list of identified indices.
    for index in indices:
        # Retrieve the character at the specific index from the original string.
        char_at_index = s[index]
        # Add the character to the list of extracted vowels.
        vowels.append(char_at_index)

    # Return the list of extracted vowels.
    return vowels


def _reconstruct_string(s: str, vowels: List[str], indices: List[int]) -> str:
    """
    Reconstructs the final string by placing the extracted vowels in reverse order
    into their original vowel positions within the input string.

    Args:
        s (str): The original input string (used as a template).
        vowels (List[str]): The list of vowels extracted in original order.
        indices (List[int]): The list of indices where vowels are located.

    Returns:
        str: The new string with vowels reversed.
    """
    # Convert the list of vowels into a list of characters for mutability.
    # We need a reverse copy of the vowels list to pop from the end.
    vowels_list: List[str] = list(vowels)
    vowels_reversed: List[str] = list(reversed(vowels_list))

    # Create a list of characters from the original string.
    # This allows us to modify individual positions without string concatenation overhead.
    characters_list: List[str] = list(s)

    # Iterate through the indices of the vowels.
    for index in indices:
        # Retrieve the character that will replace the current vowel.
        # We pop from the reversed list to get the next vowel from the end.
        new_vowel = vowels_reversed.pop()

        # Update the character at the current index in our mutable list.
        characters_list[index] = new_vowel

    # Join the list of characters back into a single string.
    return "".join(characters_list)


def reverse_vowels(s: str) -> str:
    """
    Reverses the order of vowels in a given string while keeping all other
    characters in their original positions.

    This function handles edge cases such as empty strings, strings with no
    vowels, strings with a single vowel, and strings with all vowels.
    It is case-sensitive regarding the definition of vowels (accepts both
    lowercase and uppercase).

    Args:
        s (str): The input string to process.

    Returns:
        str: A new string with the vowels reversed.
    """
    # Validate input type explicitly.
    if not isinstance(s, str):
        raise TypeError(f"Input must be a string, got {type(s).__name__}")

    # Handle the empty string edge case explicitly to avoid unnecessary processing.
    if len(s) == 0:
        return s

    # Step 1: Identify all indices where vowels occur.
    vowel_indices = _identify_vowel_indices(s)

    # Handle the case where no vowels are found.
    # The function should return the original string unchanged.
    if len(vowel_indices) == 0:
        return s

    # Step 2: Extract the vowel characters at the identified indices.
    extracted_vowels = _extract_vowels(s, vowel_indices)

    # Step 3: Reconstruct the string with vowels in reverse order.
    reversed_vowels_string = _reconstruct_string(s, extracted_vowels, vowel_indices)

    return reversed_vowels_string