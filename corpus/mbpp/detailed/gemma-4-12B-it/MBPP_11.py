from typing import List

def remove_Occ(input_string: str, char_to_remove: str) -> str:
    """
    Removes the first and last occurrence of a specific character from a string.
    If the character appears only once, that single occurrence is removed.
    If the character does not appear, the original string is returned.

    Args:
        input_string (str): The source string to process.
        char_to_remove (str): The character to be removed.

    Returns:
        str: The modified string.
    """
    # Validation: Ensure the input_string is actually a string
    if not isinstance(input_string, str):
        raise TypeError(f"Expected string for input_string, got {type(input_string).__name__}")

    # Validation: Ensure the char_to_remove is a single character string
    if not isinstance(char_to_remove, str):
        raise TypeError(f"Expected string for char_to_remove, got {type(char_to_remove).__name__}")

    if len(char_to_remove) != 1:
        raise ValueError("char_to_remove must be exactly one character long.")

    # Handle the edge case of an empty input string
    if not input_string:
        return ""

    # Find the index of the first occurrence
    first_occurrence_index = input_string.find(char_to_remove)

    # If the character is not found at all, return the original string
    if first_occurrence_index == -1:
        return input_string

    # Find the index of the last occurrence
    # rfind returns the highest index where the substring is found
    last_occurrence_index = input_string.rfind(char_to_remove)

    # Case 1: The character appears only once in the string
    # In this case, first_occurrence_index and last_occurrence_index will be the same.
    if first_occurrence_index == last_occurrence_index:
        # We construct the string by skipping only that one index
        result_parts: List[str] = []
        for i in range(len(input_string)):
            if i != first_occurrence_index:
                result_parts.append(input_string[i])
        return "".join(result_parts)

    # Case 2: The character appears at least twice
    # We need to remove the character at the first and the last index.
    # Because we are removing two distinct indices, we can safely slice.

    # If the first and last occurances are adjacent (e.g., "aa"), 
    # slicing still works correctly to remove both.

    # Logic:
    # 1. Take the part before the first occurrence.
    # 2. Take the part between the first and last occurrence.
    # 3. Take the part after the last occurrence.
    # 4. Concatenate them.

    # However, since we are removing specific indices, a more robust way
    # to handle indices is to identify which indices to KEEP.

    indices_to_keep: List[int] = []
    for i in range(len(input_string)):
        if i != first_occurrence_index and i != last_occurrence_index:
            indices_to_keep.append(i)

    result_chars: List[str] = []
    for index in indices_to_keep:
        result_chars.append(input_string[index])

    return "".join(result_chars)

# The logic above handles:
# "hello", "l" -> indices 2 and 3 are 'l'. first=2, last=3. 
# Keep indices 0, 1, 4 -> "heo"
# "abcda", "a" -> indices 0 and 4 are 'a'. first=0, last=4.
# Keep indices 1, 2, 3 -> "bcd"
# "PHP", "P"   -> indices 0 and 2 are 'P'. first=0, last=2.
# Keep index 1 -> "H"