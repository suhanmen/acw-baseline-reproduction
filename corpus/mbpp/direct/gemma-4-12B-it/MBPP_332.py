def char_frequency(input_string):
    """
    Counts the frequency of each character in a given string.

    Args:
        input_string (str): The string to analyze.

    Returns:
        dict: A dictionary where keys are characters and values are their counts.
    """
    frequency = {}
    for char in input_string:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

if __name__ == "__main__":
    assert char_frequency('python') == {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}
    assert char_frequency('program') == {'p': 1, 'r': 2, 'o': 1, 'g': 1, 'a': 1, 'm': 1}
    assert char_frequency('language') == {'l': 1, 'a': 2, 'n': 1, 'g': 2, 'u': 1, 'e': 1}