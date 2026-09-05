FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    # Input validation: Ensure the input is a string.
    if not isinstance(s, str):
        raise TypeError(f"Expected input of type 'str', but got {type(s).__name__}")

    # Handle the degenerate case of an empty string immediately.
    if len(s) == 0:
        return 0

    # Define the standard set of vowels.
    # We use a set for O(1) lookup performance.
    standard_vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    # Initialize the counter.
    vowel_count = 0

    # Iterate through every character in the string.
    # We use an index-based approach to easily check the position of 'y'.
    for index in range(len(s)):
        current_char = s[index]

        # Case 1: The character is a standard vowel.
        if current_char in standard_vowels:
            vowel_count += 1

        # Case 2: The character is 'y' or 'Y'.
        # It is only counted as a vowel if it is the last character of the word.
        elif current_char.lower() == 'y':
            is_last_character = (index == len(s) - 1)
            if is_last_character:
                vowel_count += 1

    return vowel_count

if __name__ == "__main__":
    # Verification of provided examples
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3

    # Verification of additional edge cases
    # Empty string
    assert vowels_count("") == 0
    # Single character 'y' (at the end)
    assert vowels_count("y") == 1
    # Single character 'a'
    assert vowels_count("a") == 1
    # Single character 'x'
    assert vowels_count("x") == 0
    # 'y' in the middle (should not count)
    assert vowels_count("syzygy") == 1 # only the last 'y' counts, 'y' at index 1 and 3 are ignored
    # All vowels
    assert vowels_count("aeiou") == 5
    # Mixed casing and 'y' at end
    assert vowels_count("PyThOnY") == 2 # 'o' and 'Y'