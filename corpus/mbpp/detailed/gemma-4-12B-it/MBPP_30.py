from typing import List

def count_Substring_With_Equal_Ends(s: str) -> int:
    """
    Counts all the substrings of a given string that start and end 
    with the same character. 

    Example logic:
    For "abc":
    - "a" (starts and ends with 'a')
    - "b" (starts and ends with 'b')
    - "c" (starts and ends with 'c')
    Total: 3

    For "abcda":
    - "a", "b", "c", "d", "a" (5 single characters)
    - "abcda" (starts and ends with 'a')
    Total: 6
    """

    # Input Validation: Ensure the input is a string
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")

    # Edge Case: Empty string
    # A string with no characters has zero substrings starting/ending with same char.
    if len(s) == 0:
        return 0

    # The logic follows that every single character is a valid substring 
    # (it starts and ends with itself). 
    # Furthermore, for every pair of identical characters at indices i and j 
    # where i < j, the substring s[i:j+1] is valid.

    # To solve this efficiently in O(N) time:
    # Let's count the occurrences of each character.
    # If a character appears 'k' times in the string, how many substrings 
    # start and end with that character?
    # It is the number of ways to choose 2 positions out of 'k' (for the start 
    # and end) plus the 'k' single-character substrings.
    # This is equivalent to the sum of integers from 1 to k: k * (k + 1) / 2.

    # Step 1: Count frequencies of each character
    char_frequencies = {}
    for char in s:
        if char in char_frequencies:
            char_frequencies[char] += 1
        else:
            char_frequencies[char] = 1

    # Step 2: Calculate the sum of combinations
    total_count = 0
    for char in char_frequencies:
        frequency = char_frequencies[char]

        # Use the arithmetic series sum formula: (n * (n + 1)) // 2
        # This accounts for:
        # - Substrings of length 1 (e.g., "a")
        # - Substrings of length > 1 (e.g., "a...a")
        count_for_this_char = (frequency * (frequency + 1)) // 2
        total_count += count_for_this_char

    return total_count

if __name__ == "__main__":
    # The provided assertions to verify correctness
    assert count_Substring_With_Equal_Ends("abc") == 3
    assert count_Substring_With_Equal_Ends("abcda") == 6
    assert count_Substring_With_Equal_Ends("ab") == 2