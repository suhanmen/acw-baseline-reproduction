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
    if not test:
        return {}

    counts = {}
    max_count = 0

    for letter in test.split():
        count = counts.get(letter, 0) + 1
        counts[letter] = count
        if count > max_count:
            max_count = count

    return {letter: count for letter, count in counts.items() if count == max_count}