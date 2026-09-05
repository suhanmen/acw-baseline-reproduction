def count_Substring_With_Equal_Ends(s: str) -> int:
    """
    Counts all substrings that start and end with the same character.
    Each individual character is considered a substring starting and ending with itself.
    """
    # Dictionary to store the frequency of each character
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    total_count = 0
    # For each character that appears 'n' times, the number of substrings
    # starting and ending with that character is the sum of integers from 1 to n.
    # Formula: n * (n + 1) / 2
    for count in char_counts.values():
        total_count += (count * (count + 1)) // 2

    return total_count

if __name__ == "__main__":
    assert count_Substring_With_Equal_Ends("abc") == 3
    assert count_Substring_With_Equal_Ends("abcda") == 6
    assert count_Substring_With_Equal_Ends("ab") == 2