def get_Char(s: str) -> str:
    """
    Finds the character corresponding to the sum of the positions of 
    the characters in the given string in the alphabet.
    The positions are 1-indexed (a=1, b=2, ..., z=26).
    """
    total_sum = 0
    for char in s:
        # ord('a') is 97, so ord(char) - 96 gives 1 for 'a', 2 for 'b', etc.
        total_sum += ord(char.lower()) - 96

    # The result is determined by (total_sum % 26)
    # If sum is 26, 52, etc., it corresponds to 'z' (index 0)
    # If sum is 27, 53, etc., it corresponds to 'a' (index 1)
    # Standardizing to 1-26 range:
    res_index = (total_sum - 1) % 26 + 1
    return chr(ord('a') + res_index - 1)

if __name__ == "__main__":
    assert get_Char("abc") == "f"
    assert get_Char("gfg") == "t"
    assert get_Char("ab") == "c"