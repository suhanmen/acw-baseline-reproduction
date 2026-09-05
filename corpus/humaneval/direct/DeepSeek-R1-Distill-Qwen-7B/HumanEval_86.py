def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    # Split the string into words and non-words (spaces)
    import re
    tokens = re.split(r'\s+', s)

    # Process each token: if it's a word, sort its characters; if it's a space, leave it
    processed_tokens = []
    for token in tokens:
        if token.strip() == '':  # Check if token is just whitespace
            processed_tokens.append(token)
        else:
            # Sort the characters of the word
            sorted_chars = sorted(token)
            processed_token = ''.join(sorted_chars)
            processed_tokens.append(processed_token)

    # Join the processed tokens back into a string
    return ' '.join(processed_tokens)