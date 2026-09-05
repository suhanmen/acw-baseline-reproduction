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
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    n = len(word)
    for i in range(n-2, -1, -1):
        if word[i] in vowels:
            # Check if the next two characters are consonants
            if all(word[j].lower() not in {'a', 'e', 'i', 'o', 'u'} for j in range(i+1, i+3)):
                return word[i]
    return ""