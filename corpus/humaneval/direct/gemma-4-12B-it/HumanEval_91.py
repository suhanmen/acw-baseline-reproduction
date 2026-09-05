def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.

    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    import re
    # Split the string by the delimiters '.', '?', or '!'
    # We use a regex to find the sentences.
    sentences = re.split(r'[.?!]', S)

    count = 0
    for sentence in sentences:
        # Strip leading/trailing whitespace and check if the sentence starts with "I"
        # "I" must be a standalone word, so we check if it's followed by a space or end of string
        stripped = sentence.strip()
        if stripped.startswith("I"):
            # Ensure "I" is a full word (e.g., not "Ice")
            # Check if 'I' is followed by a space or is the only word in the sentence
            if len(stripped) == 1 or stripped[1].isspace():
                count += 1

    return count