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
    sentences = S.split(['.', '?', '!'])
    # The split will create a list where the last element might be empty if the string ends with a delimiter
    # We need to check each sentence for leading "I" ignoring the delimiter
    count = 0
    for i, part in enumerate(sentences):
        if i == len(sentences) - 1 and not part and (S[-1] in '.?!'):
            continue
        # Check if the sentence starts with "I" followed by a space or is just "I"
        if part.startswith('I'):
            count += 1
    return count