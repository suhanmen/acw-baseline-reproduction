import re

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
    # Type validation: ensure input is a string
    if not isinstance(S, str):
        raise TypeError("Input must be a string.")

    # Handle empty string edge case
    if not S:
        return 0

    # Define the delimiters for sentences
    # The problem defines sentences as delimited by '.', '?', or '!'
    delimiters = {'.', '?', '!'}

    # Step 1: Split the input string into potential sentences.
    # Since delimiters are trailing, we need to ensure we handle the split 
    # such that we don't lose the last part of the text if it lacks a delimiter.

    # We use a regular expression to split by any of the three characters.
    # This will capture the text between delimiters.
    raw_sentences = re.split(r'[.?!\s]+', S)

    # However, a more robust way to handle the specific definition of 
    # "Sentences are delimited by '.', '?' or '!'" is to treat the string 
    # as a sequence of segments separated by these punctuation marks.
    # Let's refine the approach to strictly follow punctuation-based splitting.

    # We replace delimiters with a unique placeholder to split accurately
    # while preserving the segments.
    processed_string = S
    for char in delimiters:
        processed_string = processed_string.replace(char, '@@@')

    # Now split by the placeholder
    segments = processed_string.split('@@@')

    # Filter out segments that are just whitespace or empty
    # because multiple delimiters in a row or leading/trailing delimiters
    # can create empty strings in the split list.
    sentence_list = []
    for seg in segments:
        trimmed_seg = seg.strip()
        if trimmed_seg:
            sentence_list.append(trimmed_seg)

    # Step 2: Identify "boredoms"
    # A boredom is a sentence that starts with the word "I".
    # "Starts with" implies that the first token of the sentence is "I".

    boredom_count = 0

    for sentence in sentence_list:
        # Split the sentence into words to check the first word
        words = sentence.split()

        if len(words) > 0:
            first_word = words[0]

            # Check if the first word is exactly "I"
            # We use exact comparison to ensure "Ice" or "Island" aren't counted.
            if first_word == "I":
                boredom_count += 1

    return boredom_count