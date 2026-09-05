import re

def text_match_two_three(text: str) -> str:
    """
    Matches a string that contains an 'a' followed by exactly two or three 'b's.
    The 'b's can be followed by any characters, but must be exactly two or three
    immediately following the 'a'.

    Args:
        text (str): The input string to check.

    Returns:
        str: 'Found a match!' if the pattern is satisfied, otherwise 'Not matched!'.
    """
    # Validate input type
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")

    # Handle empty string edge case explicitly
    if not text:
        return "Not matched!"

    # Regex breakdown:
    # a       : Matches the literal character 'a'
    # (       : Start of a grouping for the 'b' counts
    #   bb     : Exactly two 'b's
    #   |      : OR
    #   bbb    : Exactly three 'b's
    # )       : End of grouping
    # 
    # To ensure it is exactly two or three 'b's (and not four or more),
    # we use a negative lookahead (?!b).
    # However, the requirement "a followed by two to three 'b'" usually 
    # implies that if there are 4 'b's, it does NOT match the "two to three" 
    # specific constraint in many contexts, or it matches the first 3.
    # Looking at the example: "abbbba" -> "Found a match!"
    # In "abbbba", 'a' is followed by 4 'b's. Wait, let's re-examine.
    # "abbbba" actually has 4 'b's. 
    # If the assertion says "abbbba" is a match, it means we are looking 
    # for a substring that contains 'a' followed by at least 2 and at most 3 'b's.
    # In "abbbba", the substring "abbb" matches (a + three b's).

    # Let's construct the pattern:
    # a     -> literal a
    # b{2,3} -> 2 or 3 occurrences of b
    pattern = r"abb{2,3}"

    # We use re.search to find if the pattern exists anywhere in the string.
    match_object = re.search(pattern, text)

    if match_object is not None:
        return "Found a match!"
    else:
        return "Not matched!"

# The assertions provided in the prompt:
# assert text_match_two_three("ac") == ('Not matched!')
# assert text_match_two_three("dc") == ('Not matched!')
# assert text_match_two_three("abbbba") == ('Found a match!')