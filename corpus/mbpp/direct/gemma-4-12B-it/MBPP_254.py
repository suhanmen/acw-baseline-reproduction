import re

def words_ae(s):
    """
    Finds all words starting with 'a' or 'e' in a given string.
    Note: Based on the assertions provided, the logic identifies 
    substrings starting with 'a' or 'e' that are bounded by 
    non-alphabetic characters or are parts of words where 
    sequences starting with 'a' or 'e' are extracted.

    Looking closely at the assertions:
    "python programe" -> ['ame'] (Matches 'ame' at the end of programe)
    "python programe language" -> ['ame', 'anguage']
    "assert statement" -> ['assert', 'atement']

    The logic is to find all substrings starting with 'a' or 'e' 
    that go until the end of the word or the next space/punctuation.
    """
    # Split by whitespace to get words
    words = s.split()
    results = []

    for word in words:
        # We need to find segments within the word that start with 'a' or 'e'
        # According to the assertions, these segments are usually suffixes 
        # or internal parts starting with a/e.
        # Let's check every possible starting position in the word.
        for i in range(len(word)):
            if word[i] == 'a' or word[i] == 'e':
                # Extract from this position to the end of the word
                substring = word[i:]
                # Only keep if it's not part of a larger substring already found 
                # or if it matches the assertion pattern.
                # Specifically, the assertions suggest we find occurrences 
                # where the segment starts with 'a' or 'e'.
                results.append(substring)

    # Based on the assertions, it seems we want the specific occurrences.
    # Let's refine: The pattern is substrings starting with 'a' or 'e'
    # that are not preceded by 'a' or 'e' within the same word block.

    final_results = []
    for word in words:
        # Find indices of 'a' and 'e'
        indices = [i for i, char in enumerate(word) if char == 'a' or char == 'e']
        # If there are multiple, the assertions suggest we take all that 
        # represent a distinct 'a' or 'e' start.
        # "programe" -> index 6 is 'a'. substring "ame".
        # "statement" -> index 0 is 's', index 1 is 't', index 2 is 'a'. 
        # Wait, "assert" starts with 'a' at index 0. "atement" starts at index 2.
        for idx in indices:
            # Check if this 'a' or 'e' is the start of a new "word" part
            # i.e., it's the first char of the word OR the char before it is not 'a'/'e'
            if idx == 0 or (word[idx-1] != 'a' and word[idx-1] != 'e'):
                final_results.append(word[idx:])

    return final_results

# Re-evaluating based on the assertions:
# "python programe" -> 'programe' contains 'ame' starting at index 6.
# 'a' is at index 6. word[5] is 'r'. So 'ame' is included.
# "assert" -> 'a' is at index 0. Included.
# "statement" -> 'a' is at index 2. word[1] is 't'. So 'atement' is included.

def words_ae(s):
    words = s.split()
    results = []
    for word in words:
        for i in range(len(word)):
            if word[i] in ('a', 'e'):
                # If it's the start of the word or the previous char isn't a/e
                if i == 0 or word[i-1] not in ('a', 'e'):
                    results.append(word[i:])
    return results