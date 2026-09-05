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

    # Step 1: Validate input type
    if not isinstance(s, str):
        raise TypeError(f"Expected input to be a string, got {type(s).__name__}")

    # Step 2: Handle empty string case
    if len(s) == 0:
        return 0

    # Step 3: Define the set of standard vowels (case-insensitive)
    standard_vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    # Step 4: Normalize the input string to lowercase for easier comparison
    s_lower = s.lower()

    # Step 5: Check if the string ends with 'y'
    ends_with_y = False
    if len(s_lower) > 0 and s_lower[-1] == 'y':
        ends_with_y = True

    # Step 6: Initialize counter for vowels
    vowel_count = 0

    # Step 7: Iterate through each character in the normalized string
    for i in range(len(s_lower)):
        current_char = s_lower[i]

        # Step 8: Check if the current character is a standard vowel
        if current_char in standard_vowels:
            vowel_count += 1
        # Step 9: Check if the current character is 'y' and it's at the end
        elif current_char == 'y' and i == len(s_lower) - 1 and ends_with_y:
            vowel_count += 1

    return vowel_count