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
    vowels = "aeiouAEIOU"
    # We need a vowel between two consonants.
    # A vowel at index i is valid if:
    # 1. 0 < i < len(word) - 1 (not at the start or end)
    # 2. word[i] is a vowel
    # 3. word[i-1] is NOT a vowel (is a consonant)
    # 4. word[i+1] is NOT a vowel (is a consonant)

    # We search from the right side to find the "closest" to the end.
    for i in range(len(word) - 2, 0, -1):
        char = word[i]
        if char in vowels:
            prev_char = word[i-1]
            next_char = word[i+1]
            if prev_char not in vowels and next_char not in vowels:
                return char

    return ""