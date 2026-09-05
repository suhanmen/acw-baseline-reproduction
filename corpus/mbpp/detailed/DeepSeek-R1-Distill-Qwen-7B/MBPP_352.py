def unique_characters(s):
    """Check whether all the characters in a given string are unique."""
    # Step 1: Check if the input is a string
    if not isinstance(s, str):
        return False

    # Step 2: Handle edge cases
    if len(s) == 0:
        return True
    if len(s) == 1:
        return True

    # Step 3: Collect all characters into a list
    char_list = list(s)

    # Step 4: Check for duplicates
    unique_count = len(char_list)
    unique_chars = set(char_list)
    if unique_count != len(unique_chars):
        return False

    return True