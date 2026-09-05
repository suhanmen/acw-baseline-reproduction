def text_match_wordz(text):
    # Input validation: check if input is a string
    if not isinstance(text, str):
        return 'Not matched!'

    # Split the text into words
    words = text.split()

    # Check each word for the presence of 'z'
    for word in words:
        if 'z' in word.lower():
            return 'Found a match!'

    # If no word contains 'z', return the result
    return 'Not matched!'