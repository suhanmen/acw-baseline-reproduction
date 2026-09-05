from collections import Counter

def count_common(words):
    """
    Counts the occurrences of each word in a list and returns the 
    most common words as a list of tuples, sorted by frequency 
    descending and then by original order of discovery.
    """
    counts = Counter(words)
    # Sort by frequency (descending), then preserve original order for ties
    # Python's Counter.most_common() handles the frequency part.
    # However, to match the exact expected output, we sort by count descending.
    # The test cases suggest that for equal counts, the order should be preserved.

    # Since we want to match the assertion exactly, and Counter.most_common() 
    # usually preserves insertion order for equal values in Python 3.7+
    # we check the specific expected outputs.

    # Note: In the first assertion: ('black', 5) and ('white', 5)
    # In the second: ('two', 2) and ('three', 2)
    # In the third: ('Apple', 2), ('Amazon', 2), ('Netflix', 2)
    # All these follow the order in which the words first appeared in the list.

    # most_common() returns elements in the order they were first encountered 
    # if their counts are equal.
    return counts.most_common()