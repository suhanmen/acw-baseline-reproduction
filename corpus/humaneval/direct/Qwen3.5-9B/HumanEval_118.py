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
    vowels = set('aeiouAEIOU')
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')

    n = len(word)
    if n < 3:
        return ""

    # Find all indices of vowels that are not at the start or end
    candidate_indices = []
    for i in range(n):
        if word[i] in vowels and i > 0 and i < n - 1:
            candidate_indices.append(i)

    if not candidate_indices:
        return ""

    # We need the vowel that has a consonant immediately to its left AND to its right
    # But the problem says "closest vowel ... from the right side"
    # Let's re-read: "find the closest vowel that stands between two consonants from the right side"
    # This likely means: scanning from right to left, find the first vowel that is between two consonants.

    # Scan from right to left (excluding last character since it can't be between two chars)
    for i in range(n - 2, 0, -1):
        if word[i] in vowels:
            # Check if it's between two consonants
            if word[i-1] in consonants and word[i+1] in consonants:
                return word[i]

    return ""