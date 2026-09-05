import re
from typing import Optional

VOWELS = set("aeiouAEIOU")

def is_vowel(char: str) -> bool:
    """
    Helper function to check if a character is a vowel.

    Args:
        char: A single character string.

    Returns:
        True if char is a vowel, False otherwise.
    """
    return char in VOWELS

def is_consonant(char: str) -> bool:
    """
    Helper function to check if a character is a consonant.
    Given the problem constraints (English letters only), a character is a consonant
    if it is an English letter and NOT a vowel.

    Args:
        char: A single character string.

    Returns:
        True if char is a consonant, False otherwise.
    """
    # Validate that it's an English letter before checking vowel status
    if not char.isalpha():
        return False
    return not is_vowel(char)

def find_closest_valid_vowel_from_right(word: str) -> str:
    """
    Helper function to find the closest vowel that stands between two consonants
    starting the search from the right side of the word.

    The logic iterates backwards. It looks for a sequence ending in a vowel that
    was immediately preceded by a consonant. The first such vowel encountered 
    (closest to the right) is returned.

    Specific constraints applied per problem description:
    1. Vowels at the very beginning of the word do not count.
    2. Vowels at the very end of the word do not count.
    3. The target vowel must be preceded by a consonant.
    4. The target vowel must be preceded by something that isn't the start of the string 
       (handled implicitly by checking 'previous_char') and isn't a vowel itself 
       (handled by the condition 'if prev is consonant'). 
       *Correction*: The prompt says "stands between two consonants". 
       Strictly, this means Consonant-Vowel-Consonant.
       However, usually "closest... from the right" implies we stop at the first match.
       Let's trace "yogurt" (y-o-g-u-r-t). 
       Right to left: t(con), r(con), u(vowel). Is u between two consonants?
       Preceding is 'r' (con). Following is 't' (con). Yes. Return 'u'.

       Trace "quick" (q-u-i-c-k).
       Right to left: k(con), c(con), i(vowel). Preceding 'c' (con). Following is 'u' (vowel). 
       Is 'i' between two consonants? No.
       Next: u(vowel). Preceding 'q' (con). Following is 'i' (vowel). No.
       Result: "".

       Trace "FULL". F-U-L-L. 
       Right to left: L(con), L(con), U(vowel). 
       Preceding L(con). Following L(con). Yes. Return 'U'.

       Trace "ab". a(vowel), b(con). 
       End of string check removes 'a'.
       Result: "".

    Args:
        word: The input string.

    Returns:
        The closest valid vowel string, or empty string if none found.
    """
    # Constraint Validation: Must be a string
    if not isinstance(word, str):
        return ""

    # Constraint: Empty input handling
    if len(word) == 0:
        return ""

    # We need at least 3 characters to potentially have a structure of C-V-C
    # where V is the middle one and we are looking from the right.
    # Actually, technically C-V is not enough. We need the thing to the right of V 
    # to be a consonant too? 
    # Re-reading: "stands between two consonants from the right side of the word".
    # This phrasing is slightly ambiguous.
    # Interpretation A: Find a vowel V at index i such that word[i-1] is Consonant AND word[i+1] is Consonant.
    # Interpretation B: Scan from right. The first vowel V found that has a consonant immediately to its left is the answer.
    # The examples help clarify.
    # "yogurt" -> 'u' is at index 3. 'g' (con) is left, 'r' (con) is right. Fits Interpretation A.
    # "quick" -> 'i' (idx 2). Left 'u' (vowel). Right 'c' (con). Fails A. 'u' (idx 1). Left 'q' (con). Right 'i' (vowel). Fails A.
    # "ab" -> 'a'. Right boundary. Fails.
    # "FULL" -> 'U' (idx 1). Left 'F' (con). Right 'L' (con). Fits A.

    # The phrase "from the right side" implies priority on the rightmost valid occurrence.
    # The condition "between two consonants" strongly suggests C...V...C locally.

    # Edge case: Single character. Cannot be between two consonants.
    if len(word) < 3:
        return ""

    # Edge case: All vowels or mixed such that no CVC pattern exists.

    # We iterate from the second to last character down to the second character.
    # Why not the last? Because a vowel cannot be "between" two consonants if it is the last char 
    # (nothing to the right).
    # Why not the first? Because nothing to the left.
    # So valid indices for the vowel are 1 to len-2 inclusive.

    for i in range(len(word) - 2, 0, -1):
        current_char = word[i]
        left_char = word[i - 1]
        right_char = word[i + 1]

        # Check if current is a vowel
        if not is_vowel(current_char):
            continue

        # Check if left is a consonant
        # Note: We assume input is English letters. 
        # If 'left_char' is not a letter (though problem says it will be), it's not a consonant.
        left_is_consonant = is_consonant(left_char)

        # Check if right is a consonant
        right_is_consonant = is_consonant(right_char)

        if left_is_consonant and right_is_consonant:
            # Found the closest vowel from the right satisfying C-V-C
            return current_char

    # No vowel found meeting the criteria
    return ""

def get_closest_vowel(word):
    """
    You are given a word. Your task is to find the closest vowel that stands between 
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
    # Input Validation: Explicitly handle non-string types and None
    if not isinstance(word, str):
        return ""

    # The problem statement says "You may assume that the given string contains English letter only."
    # However, robust code should handle the degenerate case of non-letters if it ever arises,
    # though the helper functions `is_consonant` already guard against non-alpha chars by returning False.
    # If the input contains spaces or numbers, they won't form valid C-V-C sequences with vowels,
    # so the logic naturally filters them out or returns empty, which is safe behavior.

    # Call the core logic
    return find_closest_valid_vowel_from_right(word)

# Additional manual test cases commented out to ensure no test code is in the final output,
# but verifying the logic mentally:
# get_closest_vowel("bcdfg") -> "" (no vowels)
# get_closest_vowel("rhythm") -> "y" (r-h-y-t-h-m? No. y-vowel? h-vowel? 
#   Actually 'y' is sometimes a vowel. But problem defines Vowels = AEIOU explicitly.
#   So 'y' is a consonant here. 'h' is consonant. No vowels. Result "").
#   Wait, standard English 'y' is tricky. Problem says "Vowels...". Usually implies a,e,i,o,u.
#   Example "yogurt" has 'u' as the target. 'y' is at start. If 'y' were vowel, it would be at start.
#   If 'y' is consonant, then 'o' (index 1) is V. Left boundary. 'u' (index 3) is V.
#   So 'u' is the only candidate. Correct.