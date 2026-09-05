import re

def text_match_one(text):
    # The pattern matches 'a' followed by one or more 'b's
    patterns = r'ab+b'

    # However, looking at the assertion "abba" == "Found a match!",
    # and the requirement "an a followed by one or more b's",
    # it implies the regex should look for 'ab+' within the string.
    # But since "abba" is expected to match, and "ac" or "dc" are not,
    # we check for the presence of 'ab' followed by at least one 'b'.

    # Let's re-evaluate the requirement: "an a followed by one or more b's".
    # Regex: 'ab+'
    # "abba" contains "abb", so it matches.
    # "ac" does not.
    # "dc" does not.

    patterns = r'ab+'

    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return 'Not matched!'

# The prompt asks for the function to be runnable and satisfy assertions.
# Based on the assertions:
# "ac" -> Not matched! (No 'ab')
# "dc" -> Not matched! (No 'ab')
# "abba" -> Found a match! (Contains 'abb')