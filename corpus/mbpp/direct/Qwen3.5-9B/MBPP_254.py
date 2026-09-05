import re

def words_ae(text: str) -> list:
    pattern = re.compile(r"\b[a-e](?:[a-z]+|$)", re.IGNORECASE)
    matches = pattern.findall(text.lower())
    # Ensure words are not just a single letter if followed by non-letter or end of string incorrectly matched
    result = []
    for match in matches:
        if len(match) > 1 or match.isalpha() and (match == match[0] + match[1:]):
            # Filter out single letters if they are not intended as full words in context, but based on assertions, we keep 'a'/'e' only if part of word
            pass
        result.append(match)
    # Re-evaluate based on test cases: "assert" starts with 'a', so full word included. "ame" and "anguage" are suffixes.
    # So we want: words starting with a/e OR substrings starting with a/e that form a word-like sequence at word boundary?
    # Looking at assertions: "python programe" -> "ame" (suffix of programe). So it's not full words only.
    # It seems to be any continuous sequence of letters that starts with 'a' or 'e' and is either:
    #   1. A full word (bounded by non-letters or start/end), OR
    #   2. A suffix that starts with a/e? No, "programe" -> "ame" means it splits the word?
    # Actually, looking closely: "python programe" -> ['ame']. "programe" ends with 'ame'.
    # "python programe language" -> ['ame','anguage']. "programe" ends with 'ame', "language" ends with 'anguage'.
    # "assert statement" -> ['assert', 'atement']. "assert" starts with 'a', "atement" is suffix of "statement".
    # Pattern: Find all maximal sequences of letters that START with 'a' or 'e'? No, because "ame" starts with 'a'.
    # But "programe" is one word, why is "ame" extracted? It seems we are extracting substrings that start with a/e
    # and go until the end of the word?
    # Let's re-read: "all words starting with 'a' or 'e'". But the examples show parts of words.
    # Maybe the problem implies: split the text by spaces, then for each word, if it contains a suffix starting with a/e?
    # Or maybe the input is not just space separated words but arbitrary strings, and we look for any alphabetic sequence
    # that starts with a or e?
    # "python programe": tokens = ["python", "programe"]. 
    #   "python" -> no.
    #   "programe" -> starts with 'p', so not a word starting with a/e. 
    #   But result is ['ame']. This contradicts "words starting with...".
    # Unless... the function splits the string into words, and then for each word, finds substrings starting with a/e?
    # No, that's too complex.
    # Alternative interpretation: The examples might be showing that we split the original string into alphabetic runs,
    # and then filter those runs that START with 'a' or 'e'.
    # Let's test this hypothesis:
    # "python programe" -> tokens by splitting on non-letters? 
    #   Actually, "programe" is one token. It starts with 'p'. So why "ame"?
    # Wait, maybe the function is: find all words (split by space) that START with 'a' or 'e', 
    # BUT the examples provided in the prompt are tricky or I am misinterpreting "words".
    # Let's look at "assert statement" -> ['assert', 'atement']. 
    # "assert" starts with 'a'. "atement" comes from "statement". "statement" starts with 's'.
    # So "atement" is NOT a full word. It's a substring.
    # Hypothesis 2: We are looking for any sequence of alphabetic characters within the string that starts with 'a' or 'e'.
    #   "python programe": 
    #     "python" -> starts with 'p'. Skip.
    #     "programe" -> starts with 'p'. Skip.
    #     But we need 'ame'. This implies "programe" is being split? Or 'ame' is a separate token?
    #   Maybe the string is treated as a sequence of words, and we check if the word STARTS with a or e?
    #   If so, "python programe" should return [] or ["programe"]? No, assertion says ['ame'].
    #   This is very confusing. Let's look at the third case: "assert statement" -> ['assert', 'atement'].
    #   "assert" matches (starts with 'a'). 
    #   "statement" does not start with 'a', but 'atement' is returned.
    #   'atement' is the suffix of "statement" starting at index 2? s-t-a-t-e-m-e-n-t. Index 2 is 'a'.
    #   So it seems we are extracting substrings that start with 'a' or 'e' and extend to the end of the word?
    #   Rule: For every word in the text, find all suffixes that start with 'a' or 'e'?
    #   Word: "programe". Suffixes: "programe" (no), "rograme" (no), "ograme" (no), "gramme" (no), "ramme" (no), "amme" (no), "me" (no), "e" (yes? but result is 'ame').
    #   Wait, 'programe' -> ... 'a' is at index 3 (0:p, 1:r, 2:o, 3:g, 4:r, 5:a, 6:m, 7,e)? 
    #   p-r-o-g-r-a-m-e. Index 5 is 'a'. Suffix from 5 is "ame". Correct.
    #   Word: "language". l-a-n-g-u-a-g-e. Index 1 is 'a'. Suffix from 1 is "anguage". Correct.
    #   Word: "assert". a-s-s-e-r-t. Index 0 is 'a'. Suffix from 0 is "assert". Correct.
    #   Word: "statement". s-t-a-t-e-m-e-n-t. Index 2 is 'a'. Suffix from 2 is "atement". Correct.
    #   Are there other 'a' or 'e' in these words?
    #   "programe": 'e' at end. Suffix "e". Why not "e" in result? Result is only ['ame']. 
    #   Maybe we only take the FIRST occurrence? Or the longest? Or specific rules?
    #   "programe": 'a' at 5, 'e' at 7. If we take first 'a'/'e' occurrence as start: 'a' -> "ame".
    #   "language": 'a' at 1. "anguage". Next 'a' at 5. Suffix "age". Not in result. So only first occurrence?
    #   "assert": 'a' at 0, 'e' at 3. First is 'a' -> "assert". Result has 'assert'. No 'er...t'? Just one per word?
    #   "statement": 'a' at 2, 'e' at 4, 'e' at 6. First is 'a' -> "atement". Result has 'atement'.
    #   Conclusion: For each word in the text, find the first occurrence of 'a' or 'e' (case-insensitive).
    #             Extract the suffix starting from that character.
    #             If no 'a' or 'e' found, ignore the word.
    #             Collect all such suffixes.
    #   Let's verify "python programe".
    #   "python": no 'a' or 'e'. Ignore.
    #   "programe": first 'a' at index 5. Suffix "ame". Add "ame".
    #   Result: ['ame']. Matches.
    #   "python programe language":
    #   "python": ignore.
    #   "programe": "ame".
    #   "language": first 'a' at index 1. Suffix "anguage".
    #   Result: ['ame', 'anguage']. Matches.
    #   "assert statement":
    #   "assert": first 'a' at 0. Suffix "assert".
    #   "statement": first 'a' at 2. Suffix "atement".
    #   Result: ['assert', 'atement']. Matches.

    # Algorithm:
    # 1. Split text into words by whitespace.
    # 2. For each word:
    #    a. Find the first index of 'a' or 'e' (case insensitive).
    #    b. If found, append word[index:] (lowercased) to result list.
    # 3. Return result.

    words = text.split()
    result = []
    for word in words:
        # Check for 'a' or 'e' in lower case
        lower_word = word.lower()
        # Find first occurrence of 'a' or 'e'
        for i in range(len(lower_word)):
            if lower_word[i] in 'ae':
                result.append(lower_word[i:])
                break
    return result

# Verification:
# assert words_ae("python programe") == ['ame']
# assert words_ae("python programe language") == ['ame','anguage']
# assert words_ae("assert statement") == ['assert', 'atement']