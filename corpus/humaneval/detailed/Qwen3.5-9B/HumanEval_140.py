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

    # --- Input Validation ---
    # Ensure the input is a string. If not, raise a TypeError immediately.
    if not isinstance(text, str):
        raise TypeError(f"Input must be a string, but received {type(text).__name__}")

    # --- Helper Function: Process a segment of text ---
    def process_replacement(match):
        """
        Processes a matched group of spaces.
        If the group length is greater than 2, returns a single '-'.
        Otherwise, it returns an underscore repeated for the length of the group.
        """
        # Get the span of the matched string to check its length
        space_sequence = match.group()
        count = len(space_sequence)

        # Determine the replacement character based on the count
        if count > 2:
            replacement_char = '-'
        else:
            replacement_char = '_'

        # Construct the new string based on the count of spaces
        if count > 2:
            # If there are more than 2 spaces, we just want one '-'
            return replacement_char
        else:
            # If there are 1 or 2 spaces, we want that many underscores
            return replacement_char * count

    # --- Execution ---
    # Check for empty or None-like strings explicitly before processing
    # The logic below handles empty strings correctly (returns empty string),
    # but we can be explicit about the flow.
    if text is None:
        raise TypeError("Input cannot be None")
    if len(text) == 0:
        return ""

    # Use Regular Expression to find all sequences of whitespace characters.
    # Note: The problem description specifically mentions "spaces".
    # To be strictly compliant with "spaces", we use ' ' instead of '\s'.
    # Pattern: r'\s+' matches one or more whitespace. 
    # However, the examples imply standard space character ' '. 
    # Let's stick to matching one or more standard space characters ' '.
    pattern = r' +'

    # Perform the substitution on the text using the helper function.
    # result_chars will hold the final characters of the processed string.
    result_chars = []

    # We can also do this via a list comprehension or direct replacement which is clearer.
    # Using regex sub is the most direct way to handle "consecutive" logic globally.
    result_text = re.sub(pattern, process_replacement, text)

    # Return the final processed string
    return result_text