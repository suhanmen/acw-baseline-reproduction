def text_match_one(text):
    # Check if the string is empty
    if len(text) == 0:
        return 'Not matched!'

    # Check if the string has only one character
    if len(text) == 1:
        return 'Not matched!'

    # Check if the string starts with 'a'
    if not text.startswith('a'):
        return 'Not matched!'

    # Check if all characters are 'a's and 'b's
    if not all(c in {'a', 'b'} for c in text):
        return 'Not matched!'

    # Check if there is at least one 'b' in the string
    if 'b' not in text:
        return 'Not matched!'

    # Check if there are no characters other than 'a' and 'b's after the initial 'a'
    # Since we already checked all characters are 'a' or 'b', this step is implied

    # If all conditions are met
    return 'Found a match!'