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
    # Replace all single spaces with underscores first
    result = text.replace(' ', '_')

    # Now collapse consecutive spaces to either single hyphens or underscores as needed
    # We can use a regular expression to handle this
    import re
    result = re.sub(r'_+(_|\Z)', '-', result)
    return result