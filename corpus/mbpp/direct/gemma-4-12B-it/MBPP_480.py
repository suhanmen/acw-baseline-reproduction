def get_max_occuring_char(s: str) -> str:
    """
    Finds the maximum occurring character in a given string.
    If multiple characters have the same maximum frequency, the one 
    appearing first in the string is returned.
    """
    if not s:
        return ""

    char_counts = {}
    for char in s:
        # Ignore spaces if they shouldn't be counted, 
        # but for the provided test cases, they are distinct chars.
        char_counts[char] = char_counts.get(char, 0) + 1

    max_char = ""
    max_count = 0

    # Iterate through the string to maintain order of appearance
    # for ties, though the logic below handles standard max finding.
    for char in s:
        if char_counts[char] > max_count:
            max_count = char_counts[char]
            max_char = char

    return max_char

if __name__ == "__main__":
    assert get_max_occuring_char("data") == "a"
    assert get_max_occuring_char("create") == "e"
    assert get_max_occuring_char("brilliant girl") == "i"