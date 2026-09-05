def count_Substring_With_Equal_Ends(s: str) -> int:
    """
    Counts the number of substrings that start and end with the same character.

    A substring starting and ending with the same character can be:
    1. A single character (e.g., 'a').
    2. A multi-character string starting and ending with the same character (e.g., 'aba').

    The formula for a character appearing n times is the number of ways to choose 
    2 positions out of n plus the n positions themselves, which is n*(n+1)/2.
    """
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    total_count = 0
    for count in char_counts.values():
        # Sum of arithmetic progression: 1 + 2 + ... + count
        total_count += (count * (count + 1)) // 2

    return total_count