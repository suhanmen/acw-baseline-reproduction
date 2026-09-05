from typing import List

def min_flip_to_make_string_alternate(s: str) -> int:
    """
    Calculates the minimum number of flips required to transform a binary 
    string into an alternating sequence (e.g., "0101..." or "1010...").

    Args:
        s (str): A string consisting only of '0' and '1'.

    Returns:
        int: The minimum number of flips required.

    Raises:
        ValueError: If the input string contains characters other than '0' or '1'.
    """
    # --- Input Validation ---
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")

    # Handle the case of an empty string
    if len(s) == 0:
        return 0

    # Validate that the string only contains '0' and '1'
    valid_chars = {'0', '1'}
    for char in s:
        if char not in valid_chars:
            raise ValueError(f"Invalid character found: '{char}'. Input must be binary.")

    # --- Logic Implementation ---
    # There are only two possible target alternating patterns for a string of length N:
    # Pattern A: Starts with '0' (e.g., "010101...")
    # Pattern B: Starts with '1' (e.g., "101010...")

    # We count how many flips are needed to reach Pattern A.
    # Any flip needed for Pattern A automatically implies the opposite flip 
    # for Pattern B at that same position.

    flips_for_pattern_a = 0
    string_length = len(s)

    for index in range(string_length):
        # Determine the expected character for Pattern A at this index.
        # Even indices should be '0', odd indices should be '1'.
        if index % 2 == 0:
            expected_char_a = '0'
        else:
            expected_char_a = '1'

        actual_char = s[index]

        # If the current character doesn't match the expected character for Pattern A,
        # increment the flip counter.
        if actual_char != expected_char_a:
            flips_for_pattern_a += 1

    # The flips needed for Pattern B is simply the difference between 
    # the total length and the flips needed for Pattern A.
    # This is because every position that matched Pattern A fails Pattern B,
    # and every position that failed Pattern A matches Pattern B.
    flips_for_pattern_b = string_length - flips_for_pattern_a

    # The answer is the minimum of the two possibilities.
    min_flips = min(flips_for_pattern_a, flips_for_pattern_b)

    return min_flips

if __name__ == "__main__":
    # Verification against provided assertions
    assert min_flip_to_make_string_alternate("0001010111") == 2
    assert min_flip_to_make_string_alternate("001") == 1
    assert min_flip_to_make_string_alternate("010111011") == 2