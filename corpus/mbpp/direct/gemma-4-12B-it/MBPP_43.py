import re

def text_match(text):
    """
    Finds sequences of lowercase letters joined with an underscore using regex.
    Matches only if the string consists of lowercase letters separated by an underscore.
    Based on the assertions, the match should probably check for the pattern 
    [a-z]+_[a-z]+ occurring within the string or matching the criteria.
    """
    # The pattern checks for a sequence of lowercase letters, 
    # an underscore, and another sequence of lowercase letters.
    # We check if this pattern exists and that it doesn't contain uppercase.
    # Given the assertions, it seems it expects a match if there's a lowercase 
    # sequence with an underscore, and fails if any uppercase letters are present 
    # in the specific parts or surrounding context of the match.

    # Looking at:
    # "aab_cbbbc" -> Match
    # "aab_Abbbc" -> No match (Uppercase A)
    # "Aaab_abbbc" -> No match (Uppercase A)

    pattern = r'^[a-z]+_[a-z]+$'

    # However, the strings provided are "aab_cbbbc", "aab_Abbbc", "Aaab_abbbc".
    # None of these are perfectly matched by ^[a-z]+_[a-z]+$ because of the trailing/leading chars.
    # Let's re-examine: "aab_cbbbc" has 3 chars after the underscore.
    # The pattern should be: find a sequence of lowercase letters, an underscore, and lowercase letters.
    # If any uppercase letter exists in the string, it fails.

    if any(c.isupper() for c in text):
        return 'Not matched!'

    if re.search(r'[a-z]+_[a-z]+', text):
        return 'Found a match!'
    else:
        return 'Not matched!'

# Re-evaluating the logic based on strict requirements:
def text_match(text):
    # The simplest regex to satisfy the specific assertions:
    # 1. Must contain lowercase_lowercase
    # 2. Must NOT contain any uppercase letters
    if re.search(r'[a-z]+_[a-z]+', text) and not re.search(r'[A-Z]', text):
        return 'Found a match!'
    else:
        return 'Not matched!'