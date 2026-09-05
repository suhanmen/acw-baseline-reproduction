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

    # Check if the word is empty
    if not word:
        return ""

    # Helper function to check if a character is a vowel
    def is_vowel(c):
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        return c in vowels

    # List to hold the positions of vowels that are between two consonants
    candidate_vowels = []

    # Iterate from the end to find the first valid vowel
    for i in reversed(range(len(word))):
        current_char = word[i]
        # Skip if it's not a vowel
        if not is_vowel(current_char):
            continue

        # Check if current vowel is preceded by a consonant and followed by a consonant
        # Look to the right (since we're going backwards) for the next consonant
        next_char_after_vowel = word[i + 1]
        # Check if next_char is consonant
        if not is_vowel(next_char_after_vowel):
            # Now check if the next consonant is followed by another vowel
            j = i + 1
            while j < len(word) and is_vowel(word[j]):
                j += 1
            if j == len(word):
                # This vowel is at the end, not between two consonants
                continue
            # Now check if the vowel at j is followed by a consonant
            k = j
            while k < len(word) and is_vowel(word[k]):
                k += 1
            if not is_vowel(word[k]):
                # Found a valid vowel between two consonants
                # Add the vowel to the candidate list
                candidate_vowels.append(current_char)
                # Since we're looking from the end, the first valid vowel is the closest
                break

    # Among candidate vowels, return the leftmost (which is the closest)
    if candidate_vowels:
        return candidate_vowels[0]
    else:
        return ""