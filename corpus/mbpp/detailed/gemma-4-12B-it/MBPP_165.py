import string

def count_char_position(input_string: str) -> int:
    """
    Counts how many characters in a given string are English alphabet letters
    at the same position as their own index in the English alphabet.

    The rule is interpreted as:
    - 'a' (index 0 in alphabet) is compared against position 0 of the string.
    - 'b' (index 1 in alphabet) is compared against position 1 of the string.
    - 'c' (index 2 in alphabet) is compared against position 2 of the string.
    - ...and so on for both uppercase and lowercase.

    Example:
    "xbcefg"
    Pos 0: 'x' (not 'a')
    Pos 1: 'b' (matches 'b' at alphabet index 1) -> +1
    Pos 2: 'c' (matches 'c' at alphabet index 2) -> +1
    Pos 3: 'e' (matches 'e' at alphabet index 4) -> No
    Pos 4: 'f' (matches 'f' at alphabet index 5) -> No
    Pos 5: 'g' (matches 'g' at alphabet index 6) -> No
    Total: 2
    """
    # Input Validation
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")

    # Handle edge case: Empty string
    if not input_string:
        return 0

    # Define the English alphabet
    # We use a 0-indexed sequence where 'a' or 'A' corresponds to 0.
    # We want to check if char at index i matches the letter at alphabet position i.
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase

    count = 0

    # Iterate through the string by index
    for index, current_char in enumerate(input_string):
        # The logic requires comparing the character at the current index 
        # with the letter that belongs at that numerical position in the alphabet.
        # Alphabet positions are 0-indexed (a=0, b=1, ... z=25).

        # If the current index is 26 or greater, it cannot match an 
        # English alphabet position (0-25).
        if index >= 26:
            continue

        # Determine what the expected character is at this position.
        # For example, at index 0, the expected characters are 'a' or 'A'.
        # At index 1, the expected characters are 'b' or 'B'.
        expected_char_lower = alphabet_lower[index]
        expected_char_upper = alphabet_upper[index]

        # Check if the current character in the string matches the 
        # expected character at this position (case-insensitive check 
        # isn't specified, but the examples show 'b' at pos 1 matches, 
        # 'C' at pos 2 matches, and 'F' at pos 5 matches).
        # Looking at the assertions:
        # "xbcefg" -> index 1 is 'b', index 2 is 'c' -> 2 matches.
        # "ABcED"  -> index 0 is 'A', index 1 is 'B', index 2 is 'c' -> 3 matches.
        # "AbgdeF" -> index 0 is 'A', index 1 is 'b', index 2 is 'g' (no), 
        #             index 3 is 'd' (no), index 4 is 'e' (no), index 5 is 'F' -> 
        #             Wait, let's re-verify the assertions.

        # Assertion 1: "xbcefg" (len 6)
        # 0:x (a), 1:b (b) MATCH, 2:c (c) MATCH, 3:e (d), 4:f (e), 5:g (f) -> count 2.

        # Assertion 2: "ABcED" (len 5)
        # 0:A (A) MATCH, 1:B (B) MATCH, 2:c (c) MATCH, 3:E (D), 4:D (E) -> count 3.

        # Assertion 3: "AbgdeF" (len 6)
        # 0:A (A) MATCH, 1:b (b) MATCH, 2:g (c), 3:d (d) MATCH, 4:e (e) MATCH, 5:F (f) MATCH
        # Note: 'd' is index 3. Alphabet 'd' is index 3. So 'd' at index 3 is a match.
        # Let's re-check "AbgdeF":
        # idx 0: 'A' matches 'A' (Match 1)
        # idx 1: 'b' matches 'b' (Match 2)
        # idx 2: 'g' matches 'c' (No)
        # idx 3: 'd' matches 'd' (Match 3)
        # idx 4: 'e' matches 'e' (Match 4)
        # idx 5: 'F' matches 'f' (Match 5)
        # Total = 5. This aligns with the assertion.

        if current_char == expected_char_lower or current_char == expected_char_upper:
            count += 1

    return count