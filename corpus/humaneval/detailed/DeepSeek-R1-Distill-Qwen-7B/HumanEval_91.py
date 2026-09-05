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
    # Edge case: if the input string is empty, return 0
    if not S.strip():
        return 0

    # Split the input into sentences using . ? ! as delimiters
    sentences = S.split( ('.', '?', '!') )

    # Edge case: if there are no sentences, return 0
    if not sentences:
        return 0

    # List to hold the counts of boredom in each sentence
    boredom_counts = []

    # Helper function to count boredom in a single sentence
    def count_boredom(sentence):
        # Split the sentence into words
        words = sentence.strip().split()
        # If the sentence is empty, return 0
        if not words:
            return 0
        # Count the number of times 'I' appears as the first word
        return sum(1 for word in words if word == 'I')

    # Iterate over each sentence and count the boredom
    for sentence in sentences:
        # Count the boredom in the current sentence
        boredom_count = count_boredom(sentence)
        # Append the count to the list
        boredom_counts.append(boredom_count)

    # Sum all the boredom counts
    total_boredom = sum(boredom_counts)

    # Return the total number of boredom
    return total_boredom