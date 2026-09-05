def first_non_repeating_character(s: str):
    """
    Finds the first non-repeated character in a given string.
    Returns None if all characters are repeated or the string is empty.
    """
    counts = {}
    # Count occurrences of each character
    for char in s:
        counts[char] = counts.get(char, 0) + 1

    # Find the first character with a count of 1
    for char in s:
        if counts[char] == 1:
            return char

    return None

if __name__ == "__main__":
    assert first_non_repeating_character("abcabc") == None
    assert first_non_repeating_character("abc") == "a"
    assert first_non_repeating_character("ababc") == "c"