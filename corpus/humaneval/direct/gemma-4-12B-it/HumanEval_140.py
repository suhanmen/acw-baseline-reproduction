import re

def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 

    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    # Check if there are any occurrences of 3 or more consecutive spaces
    if re.search(r' {3,}', text):
        # Replace all sequences of 1 or more spaces with a single dash
        # Since the prompt says "replace all consecutive spaces with -",
        # and we only do this if "more than 2 consecutive spaces" exist.
        return re.sub(r' +', '-', text)
    else:
        # Replace all spaces with underscores
        return text.replace(' ', '_')