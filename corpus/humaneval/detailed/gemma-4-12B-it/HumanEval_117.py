import string

def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    # Input Validation: Ensure s is a string and n is a non-negative integer
    if not isinstance(s, str):
        raise TypeError("The first argument 's' must be a string.")

    if not isinstance(n, int) or n < 0:
        # The problem specifies n as a natural number (usually 0, 1, 2...).
        # We handle negative numbers as invalid inputs.
        raise ValueError("The second argument 'n' must be a non-negative integer.")

    # Handle edge case: Empty string
    if not s:
        return []

    def count_consonants(word: str) -> int:
        """Helper function to count consonants in a word.
        Consonants are letters that are not vowels.
        """
        vowels = set("aeiouAEIOU")
        count = 0
        for char in word:
            # Check if the character is a letter and not a vowel
            if char.isalpha() and char not in vowels:
                count += 1
        return count

    # Step 1: Tokenize the string into words based on spaces.
    # .split() without arguments handles multiple spaces and leading/trailing spaces.
    raw_words = s.split()

    # Step 2: Filter the words based on the consonant count.
    result = []
    for word in raw_words:
        # Even if words contain punctuation (though prompt says letters and spaces),
        # we treat the sequence of letters as the word unit.
        current_consonant_count = count_consonants(word)

        # Check if the count matches the required n
        if current_consonant_count == n:
            result.append(word)

    return result