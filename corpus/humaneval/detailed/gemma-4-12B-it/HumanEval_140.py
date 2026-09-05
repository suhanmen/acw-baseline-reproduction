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
    # Validate input type: The problem implies text should be a string.
    if not isinstance(text, str):
        raise TypeError(f"Input must be a string, but received {type(text).__name__}")

    # Handle empty string edge case explicitly.
    if text == "":
        return ""

    # Step 1: Identify areas with more than 2 consecutive spaces.
    # We need to decide which segments become '-' and which become '_'.
    # A specific rule is given: 
    # "if a string has more than 2 consecutive spaces, then replace all consecutive spaces with -"
    # This implies a global check: if ANY part of the string has 3+ spaces, 
    # the transformation logic for ALL consecutive spaces might change, 
    # OR it applies locally to those specific sequences.
    # Looking at the example " Example   3" -> "_Example-3", 
    # " Example" became "_Example" (single space -> underscore)
    # "   3" became "-3" (triple space -> dash).
    # This confirms the rule is local to the consecutive sequence.

    # We will use a regular expression to find all sequences of spaces.
    # This allows us to process each group of spaces independently.
    space_sequences = re.findall(r' +', text)

    # If there are no spaces at all, return the original text.
    if not space_sequences:
        return text

    # We will build the result by iterating through the string and 
    # replacing sequences of spaces based on their length.
    # However, a simple regex substitution with a callback is the most robust 
    # way to handle overlapping/adjacent logic without messy index tracking.

    def replacement_logic(match):
        """
        Helper function to determine the replacement for a found sequence of spaces.
        """
        sequence = match.group(0)
        sequence_length = len(sequence)

        if sequence_length > 2:
            # Rule: if more than 2 consecutive spaces, replace all consecutive spaces with -
            # Note: The prompt says "replace all consecutive spaces with -".
            # Usually, this means the entire block of spaces becomes a single dash.
            return "-"
        else:
            # Rule: replace all spaces with underscores.
            # For 1 or 2 spaces, we replace each individual space with an underscore.
            # " " -> "_"
            # "  " -> "__"
            return "_" * sequence_length

    # Use re.sub with a callback function to process every space block found.
    # This ensures that "   " is caught as one block and processed as "-".
    # And " " is caught as one block and processed as "_".
    result = re.sub(r' +', replacement_logic, text)

    return result