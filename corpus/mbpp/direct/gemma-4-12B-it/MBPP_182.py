import re

def find_character(string):
    """
    Finds uppercase, lowercase, special characters, and numeric values in a string using regex.

    Args:
        string (str): The input string to analyze.

    Returns:
        tuple: A tuple containing four lists: (uppercase, lowercase, numbers, special_characters)
               Note: Based on the provided assertions, the order of the return is (uppercase, lowercase, numbers, special_characters).
               However, the assertions specifically map '2' and '32' to the third list, which represents numbers.
    """
    uppercase = re.findall(r'[A-Z]', string)
    lowercase = re.findall(r'[a-z]', string)
    numbers = re.findall(r'[0-9]', string)
    special_chars = re.findall(r'[^A-Za-z0-9]', string)

    # Adjusting logic to match the specific assertion behavior:
    # Assertion 2: "Hithere2" -> (['H'], ['i', 't', 'h', 'e', 'r', 'e'], ['2'], [])
    # This implies the 3rd element is numbers and the 4th is special characters.

    # Re-evaluating the assertions provided in the prompt:
    # find_character("Hithere2") == (['H'], ['i', 't', 'h', 'e', 'r', 'e'], ['2'], [])
    # Wait, looking closely at "Hithere2" -> 'i', 't', 'h', 'e', 'r', 'e' is 6 letters. 
    # The string "Hithere2" has 8 chars. 'H' (1), 'i' (2), 't' (3), 'h' (4), 'e' (5), 'r' (6), 'e' (7), '2' (8).
    # In "Hithere2", if 'H' is uppercase and 'i,t,h,e,r,e' are lowercase, that is 7 chars.
    # The string "Hithere2" has: H(U), i(L), t(L), h(L), e(L), r(L), e(L), 2(N). Total 8.
    # My count was slightly off. Let's re-verify:
    # "Hithere2" -> H(U), i,t,h,e,r,e(L), 2(N). That is 1 U, 6 L, 1 N.
    # The assertion says (['H'], ['i', 't', 'h', 'e', 'r', 'e'], ['2'], []).
    # This matches perfectly.

    return (uppercase, lowercase, numbers, special_chars)