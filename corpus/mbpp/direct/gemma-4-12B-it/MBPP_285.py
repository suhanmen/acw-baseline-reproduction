import re

def text_match_two_three(text):
    # The regex matches 'a' followed by exactly 2 or 3 'b's
    # We use a lookahead or specific boundaries to ensure it doesn't match 4 'b's
    # However, the provided test case "abbbba" suggests we are looking for the 
    # presence of the pattern "abb" or "abbb" within the string.
    # To strictly match "a" followed by 2 or 3 "b"s (and not 4), 
    # we ensure the character after the 'b's is not another 'b'.

    pattern = r'a(bbb?)(?![b])'

    if re.search(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'