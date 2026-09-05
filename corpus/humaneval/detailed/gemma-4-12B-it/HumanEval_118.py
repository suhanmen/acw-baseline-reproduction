def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).

    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    # Defensive Programming: Validate input type
    if not isinstance(word, str):
        raise TypeError("Input must be a string.")

    # Edge Case: Empty string, string too short to have a middle character
    # Minimum length for a middle character between two neighbors is 3.
    if len(word) < 3:
        return ""

    vowels_set = set("aeiouAEIOU")

    def is_vowel(char: str) -> bool:
        """Helper to check if a character is a vowel."""
        return char in vowels_set

    def is_consonant(char: str) -> bool:
        """Helper to check if a character is a consonant."""
        # Problem states input contains English letters only.
        # A consonant is any letter that is not a vowel.
        return char.isalpha() and char not in vowels_set

    # We need to find the vowel closest to the right side.
    # This means we should iterate from the second-to-last character 
    # backwards towards the second character (index 1).
    # The first character (index 0) and last character (index n-1) 
    # cannot be the "middle" character.

    # Indices to check: 1 to len(word) - 2
    # Range starts from the right (the largest index) and moves left.
    word_length = len(word)

    # Start index: word_length - 2 (the second to last character)
    # End index: 1 (the second character)
    # We iterate backwards from word_length - 2 down to 1.
    for i in range(word_length - 2, 0, -1):
        current_char = word[i]

        # Check if the current character is a vowel
        if is_vowel(current_char):
            # Check the character to the left
            char_left = word[i - 1]
            # Check the character to the right
            char_right = word[i + 1]

            # Condition: Vowel must stand between two consonants
            left_is_consonant = is_consonant(char_left)
            right_is_consonant = is_consonant(char_right)

            if left_is_consonant and right_is_consonant:
                # Since we are iterating from right to left, 
                # the first one we find is the closest from the right side.
                return current_char

    # If the loop completes without returning, no such vowel exists.
    return ""