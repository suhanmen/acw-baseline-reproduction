from typing import List


def count_Substring_With_Equal_Ends(s: str) -> int:
    """
    Counts the number of substrings where the first and last characters are the same.

    A substring is defined as a contiguous sequence of characters. 
    For example, in "aba", the substrings are:
    'a', 'b', 'a', 'ab', 'ba', 'aba'
    Substrings with same first/last: 'a', 'b', 'a', 'aba' -> Total 4.

    Logic:
    If a character appears 'n' times in a string, the number of substrings 
    starting and ending with that character is the number of ways to choose 
    two indices (i, j) such that i <= j and s[i] == s[j].
    This is equivalent to the sum of the first n natural numbers: n * (n + 1) / 2.
    """

    # Input Validation: Ensure the input is a string.
    if not isinstance(s, str):
        raise TypeError(f"Expected input of type str, but received {type(s).__name__}")

    # Handle the edge case of an empty string.
    if len(s) == 0:
        return 0

    # Dictionary to store the frequency of each character encountered in the string.
    char_frequencies: dict[str, int] = {}

    # Count the occurrences of each character.
    for char in s:
        if char in char_frequencies:
            char_frequencies[char] += 1
        else:
            char_frequencies[char] = 1

    total_count: int = 0

    # Calculate the number of valid substrings for each unique character.
    # For a character appearing 'n' times:
    # Number of substrings = (n * (n + 1)) // 2
    for char in char_frequencies:
        count = char_frequencies[char]

        # A character appearing once yields 1 substring (the character itself).
        # A character appearing twice yields 3 substrings (two singles, one double).
        # A character appearing three times yields 6 substrings (three singles, 
        # two doubles, one triple).
        # This follows the triangular number formula.
        pair_combinations = (count * (count + 1)) // 2
        total_count += pair_combinations

    return total_count


if __name__ == "__main__":
    # Test cases provided in the prompt
    assert count_Substring_With_Equal_Ends('aba') == 4
    assert count_Substring_With_Equal_Ends('abcab') == 7
    assert count_Substring_With_Equal_Ends('abc') == 3

    # Additional edge cases
    assert count_Substring_With_Equal_Ends('') == 0
    assert count_Substring_With_Equal_Ends('aaaaa') == 15  # 5*6/2
    assert count_Substring_With_Equal_Ends('abcde') == 5