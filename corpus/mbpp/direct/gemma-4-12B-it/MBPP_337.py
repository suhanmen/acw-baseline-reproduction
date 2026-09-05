import re

def text_match_word(text):
    # Match the word "python" specifically at the end of the string
    # followed by optional punctuation (non-word characters)
    # and optional whitespace.
    # ^ asserts start, $ asserts end.
    # Using a regex that looks for 'python' followed by optional non-word chars at the end.
    pattern = r"python\W*$"

    if re.search(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'