from typing import List

def minimum_Length(s: str) -> int:
    """
    Finds the minimum possible length of the string after removing all 
    occurrences of exactly one unique character from the input string.

    Logic:
    To minimize the resulting string length, we must identify which character 
    appears most frequently in the string and remove all instances of that character.

    Args:
        s (str): The input string to process.

    Returns:
        int: The length of the string after removing the most frequent character.

    Raises:
        ValueError: If the input is not a string.
    """
    # Input Validation
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")

    # Handle edge case: Empty string
    # If the string is empty, removing any "one character" results in a length of 0.
    # However, logically, if there are no characters to pick, the length remains 0.
    if len(s) == 0:
        return 0

    # Step 1: Count occurrences of every character in the string
    # We use a dictionary to map character -> count
    char_counts = {}
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    # Step 2: Determine the maximum frequency
    # This represents the maximum number of characters we can remove 
    # by choosing a single unique character type.
    max_frequency = 0
    for count in char_counts.values():
        if count > max_frequency:
            max_frequency = count

    # Step 3: Calculate resulting length
    # The resulting length is the original length minus the count of the 
    # character we chose to remove.
    original_length = len(s)
    min_result_length = original_length - max_frequency

    return min_result_length

# Verification against provided assertions:
# "mnm" -> 'm' appears 2 times, 'n' appears 1 time. 
# Remove 'm' (2) -> length is 1.
# "abcda" -> 'a' appears 2 times, others 1. 
# Remove 'a' (2) -> length is 3.
# "abcb" -> 'b' appears 2 times, others 1. 
# Remove 'b' (2) -> length is 2.