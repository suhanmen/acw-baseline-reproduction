def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.

    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}
    """

    # Handle empty input
    if not test:
        return {}

    # Split the input string into parts
    parts = test.split()

    # Validate the input parts
    for part in parts:
        if not part or not part.isalpha() or len(part) != 1:
            raise ValueError("Invalid input format: parts must be single characters")

    # Count occurrences of each letter
    counts = {}
    for char in parts:
        counts[char] = counts.get(char, 0) + 1

    # Find the maximum count value
    if not counts:
        return {}
    max_count = max(counts.values())

    # Collect all letters with the maximum count
    max_letters = [letter for letter, count in counts.items() if count == max_count]

    # Prepare the result dictionary
    result = {letter: max_count for letter in max_letters}

    return result