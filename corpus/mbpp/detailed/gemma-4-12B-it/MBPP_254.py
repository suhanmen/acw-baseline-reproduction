import re
from typing import List


def words_ae(input_string: str) -> List[str]:
    """
    Identifies all substrings within a given string that start with the 
    characters 'a' or 'e'. The definition of a "word" in this context, 
    based on the provided test cases, is any continuous sequence of 
    alphabetic characters that begins with 'a' or 'e'.

    Note: Based on the assertions:
    - "programe" -> 'ame' (starts with 'a', the 'e' is ignored because it's a suffix)
    - "language" -> 'anguage' (starts with 'a', the 'e' is ignored)
    - "assert statement" -> 'assert' (starts with 'a') and 'atement' (starts with 'a')

    Looking closely at the assertions:
    "python programe" -> ['ame'] implies 'ame' is the word.
    "python programe language" -> ['ame', 'anguage']
    "assert statement" -> ['assert', 'atement']

    Interpretation: A "word" is a sequence of letters. If a sequence of 
    letters contains a position where a letter is 'a' or 'e', and the 
    letters following it form a valid alphabetic block, that block is 
    considered a word starting with 'a' or 'e'. However, the assertions
    suggest we are looking for sequences starting with 'a' or 'e' that are
    delimited by non-alphabetic characters OR by the start of the string.

    Wait, looking at "programe" -> "ame". 
    The 'a' is at index 6. The 'e' is at index 7. 
    If the word was "ame", it starts at index 6 and ends at 8.
    In "assert statement", "assert" starts at 0, "atement" starts at 7.

    Refined Logic: Find all maximal contiguous blocks of alphabetic characters.
    Within each block, identify every occurrence of 'a' or 'e'.
    For every such occurrence, the "word" is the substring from that 
    occurrence to the end of that specific alphabetic block.
    """

    # Input Validation
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string.")

    if input_string is None:
        return []

    # Step 1: Identify all maximal contiguous alphabetic blocks.
    # We use a regex to find sequences of [a-zA-Z].
    # This handles spaces, punctuation, and numbers as delimiters.
    blocks = re.findall(r'[a-zA-Z]+', input_string)

    results = []

    # Step 2: Iterate through each block found.
    for block in blocks:
        # Step 3: Within each block, find indices where 'a' or 'e' occurs.
        # We must check both lowercase and uppercase if the problem implies it,
        # but the assertions only show lowercase. To be safe and precise 
        # to the assertions, we check 'a' and 'e'.
        for index, char in enumerate(block):
            if char == 'a' or char == 'e':
                # The "word" is from this index to the end of this block.
                word_fragment = block[index:]

                # Requirement check: The assertions show "ame" from "programe".
                # If we took "programe" and found 'a', we get "ame".
                # If we took "programe" and found 'e', we get "e".
                # However, the assertion says only ['ame'].
                # This implies that if a word starts with 'a' or 'e', 
                # and is followed by more letters, it is captured.
                # But 'e' at the end of "programe" is not captured.
                # Actually, the most consistent rule for the assertions is:
                # For every alphabetic block, find all positions of 'a' or 'e'.
                # The word is the substring from that position to the end of the block.
                # EXCEPTION: If that substring is just "e" and it's at the very end,
                # or if it's a single "e", does it count?
                # "programe" -> 'ame' (starts at 'a'). If it counted 'e', it would be ['ame', 'e'].
                # Since it's only ['ame'], 'e' at the end is excluded.

                # Let's re-examine "assert statement" -> ['assert', 'atement'].
                # "assert" is a block. 'a' is at index 0. Result: "assert".
                # "statement" is a block. 'a' is at index 2. Result: "atement".
                # The 'e' in "assert" is at index 4. If it were included, 
                # the result would be ['assert', 'ert', 'atement'].
                # Since 'ert' is not there, it means 'e' at index 4 is ignored.

                # New Rule: A word starts at 'a' or 'e' ONLY IF the character
                # immediately preceding it is NOT a letter (it's the start of a block)
                # OR if it's a specific type of word.

                # Let's try: Find every occurrence of 'a' or 'e'. 
                # If it is at the start of a contiguous alphabetic block, 
                # that block is a word.
                pass

    # RE-EVALUATING ASSERTIONS AGAIN:
    # "python programe" -> ['ame']
    # "python programe language" -> ['ame', 'anguage']
    # "assert statement" -> ['assert', 'atement']

    # Let's look at "programe":
    # p r o g r a m e
    # 0 1 2 3 4 5 6 7
    # 'a' is at index 5. The substring from 5 to the end is "ame".
    # 'e' is at index 7. The substring from 7 to the end is "e".
    # The result is ['ame']. Why is 'e' excluded?
    # Maybe because "ame" is a "word" and "e" is too short? No, "e" is a letter.
    # Maybe because "e" is at the very end?

    # Let's look at "assert":
    # a s s e r t
    # 0 1 2 3 4 5
    # 'a' is at index 0. Substring: "assert".
    # 'e' is at index 3. Substring: "ert".
    # The result is ['assert']. Why is "ert" excluded?

    # HYPOTHESIS: The "word" is the substring starting at 'a' or 'e' 
    # that continues until the end of the alphabetic block, 
    # BUT only if the 'a' or 'e' is preceded by a non-alphabetic character
    # OR if it's the very first letter of the string.
    # Wait, "statement" -> "atement". 
    # "statement" is one block. 
    # 'a' is at index 2. It is preceded by 't'.
    # So the "start of block" rule is wrong.

    # Let's look at "statement" again.
    # s t a t e m e n t
    # 0 1 2 3 4 5 6 7 8
    # 'a' is at 2. Substring: "atement".
    # 'e' is at 4. Substring: "ement".
    # 'e' is at 6. Substring: "ent".
    # Only "atement" is in the result.

    # Why "atement" and not "ement" or "ent"?
    # They all start with 'e'.
    # Is there a rule about the character before 'a' or 'e'?
    # In "statement", 'a' is preceded by 't'.
    # In "programe", 'a' is preceded by 'r'.
    # In "assert", 'a' is preceded by nothing (start of string).
    # In "language", 'a' is preceded by 'u' (Wait, l a n g u a g e).
    # Let's re-count "language":
    # l a n g u a g e
    # 0 1 2 3 4 5 6 7
    # 'a' is at 1. Substring: "anguage".
    # 'a' is at 5. Substring: "age".
    # 'e' is at 7. Substring: "e".
    # Assertion says: ['ame', 'anguage'].
    # So "age" and "e" are excluded.

    # Let's look at the commonalities:
    # "ame" (from programe) - 'a' is preceded by 'r'
    # "anguage" (from language) - 'a' is preceded by 'l' (Wait, index 1)
    # "assert" (from assert) - 'a' is preceded by nothing
    # "atement" (from statement) - 'a' is preceded by 't'

    # All these starts are 'a'. None of them are 'e'.
    # Does the problem actually mean words starting with 'a' or 'e' 
    # but specifically only 'a' in these cases? No, the prompt says 'a' or 'e'.
    # Let's look at the string "programe" again. 
    # If "ame" is the result, and the 'a' is at index 5...
    # What if the rule is: The word must start with 'a' or 'e', 
    # and it must be the FIRST occurrence of 'a' or 'e' in a contiguous 
    # alphabetic block?

    # Test "programe" with "First 'a' or 'e' in block" rule:
    # Block is "programe". First 'a' or 'e' is 'a' at index 5.
    # Result: "ame". Correct!

    # Test "language" with "First 'a' or 'e' in block" rule:
    # Block is "language". First 'a' or 'e' is 'a' at index 1.
    # Result: "anguage". Correct!

    # Test "assert statement" with "First 'a' or 'e' in block" rule:
    # Block 1: "assert". First 'a' or 'e' is 'a' at index 0. Result: "assert".
    # Block 2: "statement". First 'a' or 'e' is 'a' at index 2. Result: "atement".
    # Result: ['assert', 'atement']. Correct!

    # This rule perfectly matches all assertions.

    # Final Logic:
    # 1. Split string into blocks of alphabetic characters.
    # 2. For each block, find the index of the first occurrence of 'a' or 'e'.
    # 3. If found, take the substring from that index to the end of the block.
    # 4. Collect and return.

    blocks = re.findall(r'[a-zA-Z]+', input_string)
    final_results = []

    for block in blocks:
        first_idx = -1
        for i, char in enumerate(block):
            if char == 'a' or char == 'e':
                first_idx = i
                break

        if first_idx != -1:
            word = block[first_idx:]
            final_results.append(word)

    return final_results