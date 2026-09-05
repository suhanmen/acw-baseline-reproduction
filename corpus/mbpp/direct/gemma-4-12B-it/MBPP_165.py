def count_char_position(s: str) -> int:
    """
    Counts characters in a string that are at a position (1-indexed)
    corresponding to their alphabetical order (A=1, B=2, ..., Z=26).
    The comparison is case-insensitive for the alphabet check.
    """
    count = 0
    for i, char in enumerate(s):
        # Position is 1-indexed
        position = i + 1

        # Check if the character is an English letter
        if char.isalpha():
            # Convert character to its position in the alphabet (1-26)
            # ord('a') is 97, ord('A') is 65
            if char.islower():
                char_pos = ord(char) - ord('a') + 1
            else:
                char_pos = ord(char) - ord('A') + 1

            # If the position in the string matches the alphabet position
            if char_pos == position:
                count += 1
    return count